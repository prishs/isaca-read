#!/usr/bin/env python3
"""Pre-fetch RSS feeds and CISA KEV JSON for the daily digest workflow."""

from __future__ import annotations

import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape
from typing import Iterable

USER_AGENT = "isaca-read/1.0 (+https://github.com/prishs/isaca-read)"


@dataclass(frozen=True)
class Feed:
    source: str
    url: str
    kind: str = "rss"  # rss | kev


FEEDS: tuple[Feed, ...] = (
    # RSS/KEV only — sources with no CI-friendly feed are handled by the
    # research agent (ISACA Now blog, Cyber Security Headlines, regulatory).
    Feed("CISA advisories", "https://www.cisa.gov/cybersecurity-advisories/all.xml"),
    Feed("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    Feed("BleepingComputer", "https://www.bleepingcomputer.com/feed/"),
    Feed("Krebs on Security", "https://krebsonsecurity.com/feed/"),
    Feed("SANS ISC (diaries + Stormcast)", "https://isc.sans.edu/rssfeed_full.xml"),
    Feed("CISA KEV catalog", "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json", "kev"),
)


@dataclass
class Item:
    source: str
    title: str
    url: str
    published: date
    summary: str = ""


def parse_pubdate(raw: str | None) -> date | None:
    if not raw:
        return None
    raw = raw.strip()
    for parser in (
        lambda s: parsedate_to_datetime(s).astimezone(timezone.utc).date(),
        lambda s: datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc).date(),
        lambda s: datetime.strptime(s[:10], "%Y-%m-%d").date(),
    ):
        try:
            return parser(raw)
        except (ValueError, TypeError, OverflowError):
            continue
    return None


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    for _ in range(2):
        text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def fetch_bytes(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _local_name(tag: str) -> str:
    if tag.startswith("{"):
        return tag.rsplit("}", 1)[1]
    return tag


def _child_text(node: ET.Element, name: str) -> str:
    val = node.findtext(name)
    if val:
        return val.strip()
    for child in node:
        if _local_name(child.tag) == name and child.text:
            return child.text.strip()
    return ""


def _feed_entries(root: ET.Element) -> list[ET.Element]:
    channel = root.find("channel")
    if channel is not None:
        items = channel.findall("item")
        if items:
            return items
    for pattern in (".//{*}item", ".//item", ".//{*}entry", ".//entry"):
        nodes = root.findall(pattern)
        if nodes:
            return nodes
    return []


def _entry_link(node: ET.Element) -> str:
    link_text = _child_text(node, "link")
    if link_text.startswith("http"):
        return link_text
    alternate = ""
    for child in node:
        if _local_name(child.tag) != "link":
            continue
        href = (child.get("href") or "").strip()
        if not href:
            continue
        rel = child.get("rel", "alternate")
        if rel == "alternate":
            return href
        if not alternate:
            alternate = href
    return alternate


def _entry_pubdate(node: ET.Element) -> str | None:
    for name in ("pubDate", "published", "updated"):
        val = _child_text(node, name)
        if val:
            return val
    return None


def _entry_summary(node: ET.Element) -> str:
    for name in ("description", "summary", "content"):
        val = _child_text(node, name)
        if val:
            return val
    encoded = node.findtext("{http://purl.org/rss/1.0/modules/content/}encoded")
    return encoded or ""


def kev_detail_url(cve: str) -> str:
    if re.fullmatch(r"CVE-\d{4}-\d+", cve):
        return f"https://nvd.nist.gov/vuln/detail/{cve}"
    return "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"


def parse_rss(source: str, body: bytes, cutoff: date) -> list[Item]:
    root = ET.fromstring(body)
    items: list[Item] = []
    for node in _feed_entries(root):
        title = strip_html(_child_text(node, "title"))
        link = _entry_link(node)
        if not title or not link:
            continue
        pub = parse_pubdate(_entry_pubdate(node))
        if pub is None or pub < cutoff:
            continue
        summary = strip_html(_entry_summary(node))
        items.append(Item(source=source, title=title, url=link, published=pub, summary=summary[:280]))
    return items


def parse_kev(source: str, body: bytes, cutoff: date) -> list[Item]:
    data = json.loads(body)
    items: list[Item] = []
    for entry in data.get("vulnerabilities", []):
        added = parse_pubdate(entry.get("dateAdded"))
        if added is None or added < cutoff:
            continue
        cve = entry.get("cveID") or "Unknown CVE"
        name = entry.get("vulnerabilityName") or entry.get("shortDescription") or cve
        vendor = entry.get("vendorProject") or ""
        product = entry.get("product") or ""
        title = f"{cve}: {name}"
        summary = f"Added to KEV on {added.isoformat()}"
        vendor_product = " ".join(p.strip() for p in (vendor, product) if p and p.strip())
        if vendor_product:
            summary += f" — {vendor_product}"
        due = entry.get("dueDate")
        if due:
            summary += f"; federal remediation due {due}"
        items.append(
            Item(
                source=source,
                title=title,
                url=kev_detail_url(cve),
                published=added,
                summary=summary,
            )
        )
    return items


def collect_items(cutoff: date) -> tuple[list[Item], list[str]]:
    items: list[Item] = []
    errors: list[str] = []
    for feed in FEEDS:
        try:
            body = fetch_bytes(feed.url)
            if feed.kind == "kev":
                items.extend(parse_kev(feed.source, body, cutoff))
            else:
                items.extend(parse_rss(feed.source, body, cutoff))
        except (OSError, ET.ParseError, json.JSONDecodeError) as exc:
            errors.append(f"- {feed.source} ({feed.url}): {exc}")
    items.sort(key=lambda i: (i.published, i.source, i.title), reverse=True)
    return items, errors


def render_markdown(items: Iterable[Item], cutoff: date, today: date, errors: Iterable[str]) -> str:
    lines = [
        "# Pre-fetched source candidates",
        "",
        f"Window: **{cutoff.isoformat()}** through **{today.isoformat()}** (inclusive).",
        "Use these as the primary candidate list. Prefer them over ad-hoc browsing.",
        "",
    ]
    if errors:
        lines.extend(["## Fetch warnings", *errors, ""])

    if not items:
        lines.append("_No dated items found in RSS/KEV feeds for this window._")
        return "\n".join(lines) + "\n"

    lines.append("## Candidates")
    current_day: date | None = None
    for item in items:
        if item.published != current_day:
            current_day = item.published
            lines.extend(["", f"### {current_day.isoformat()}", ""])
        summary = f" — {item.summary}" if item.summary else ""
        lines.append(f"- **{item.source}:** {item.title} ([link]({item.url})){summary}")
    return "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} CUTOFF_DATE TODAY OUTPUT_MD", file=sys.stderr)
        return 2
    cutoff = date.fromisoformat(sys.argv[1])
    today = date.fromisoformat(sys.argv[2])
    output = sys.argv[3]
    items, errors = collect_items(cutoff)
    content = render_markdown(items, cutoff, today, errors)
    with open(output, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"Wrote {len(items)} candidate(s) to {output}")
    if errors:
        print(f"Warnings: {len(errors)} feed(s) failed", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
