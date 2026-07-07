# Daily Security & Audit Digest — Agent Instructions

You are generating today's cybersecurity news digest for a CISO, VAPT Specialist, CISA-Certified IS/IT Auditor. Today's date is **{{DATE}}**.

## Task

Research the past 24–48 hours of security news using web search/fetch, then write a single Markdown file at `digests/{{DATE}}.md`. Do not modify any other files.

## Sources to sweep

- US CISA: new alerts, advisories, and Known Exploited Vulnerabilities (KEV) catalog additions
- The Hacker News, BleepingComputer — major incidents and vulnerabilities
- Krebs on Security — investigative pieces
- SANS Internet Storm Center — daily diary highlights
- ISACA Now blog — audit/GRC items
- Regulatory news: SEC cyber disclosure, EU NIS2/DORA, major data-protection rulings

## Daily podcast briefings

Also summarize today's (or the latest) episode of these two daily shows, from their show notes / episode pages:

- **SANS Stormcast** (isc.sans.edu/podcast.html) — 5-minute technical brief
- **Cyber Security Headlines** (CISO Series) — daily news headlines

## Research efficiency (do not skip content — just fetch smart)

- Fetch each source's index/show-notes page once; do not fetch full articles when the headline + summary already gives you what the digest entry needs.
- Prefer show notes and episode descriptions over full transcripts — only open a transcript if the notes are too thin to extract takeaways.
- When a podcast covers a story you already have from a news source (or vice versa), analyze it once and reuse — do not re-fetch or re-read the same story from a second outlet unless the coverage genuinely differs.
- These rules cut research cost only. They must NOT shrink the written digest: keep the full output format and item counts below.

## Selection & ranking

Pick the 5–10 most relevant items. Rank by relevance to **consulting, IS (information systems) audit, and CISO work**: actively exploited vulnerabilities, breaches with control-failure lessons, regulatory changes, and framework/standard updates rank highest; items with security-program or board-level impact (major vendor/platform decisions, budget-shifting threat trends, sector-wide risks) also rank high; new public PoCs/exploits, attack techniques, and notable vulnerability write-ups relevant to VAPT engagements also rank high; generic product news ranks lowest. Deduplicate stories covered by multiple outlets — one entry, best source linked.

## Output format for `digests/{{DATE}}.md`

```markdown
---
title: "Digest {{DATE}}"
---

# Security & Audit Digest — {{DATE}}

## Top items

### 1. <Headline>
**Why it matters for audit/consulting/CISO:** <1–2 sentences>
<2–3 sentence summary> ([source](url))

### 2. ...

## Quick hits
- <one-liner> ([source](url))
- ...

## Podcast briefings
### SANS Stormcast — <episode title> (<date>)
- <takeaway 1>
- <takeaway 2>

[Episode](url)

### Cyber Security Headlines — <episode title> (<date>)
- <takeaway 1>
- <takeaway 2>

[Episode](url)

## Regulatory & framework watch
- <item or "Nothing new today">
```

In the podcast sections, cite the briefing source (episode page link) even when a story also appears under Top items; cross-reference instead of repeating ("covered in item 2 above" is fine as a bullet).

## Rules

- Every item must have a real, working source link you actually found — never invent URLs or stories.
- Links must point to the specific article or episode page, never to a site homepage or show page. If you cannot find the specific URL, either drop the item or mark it explicitly with "(specific link not found)" so the reader knows it is unverified.
- If research tools fail entirely, still write the file with a note: "Digest generation failed — sources unreachable."
- Keep the whole digest under ~800 words. Plain, direct language.
