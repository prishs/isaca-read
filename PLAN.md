# ISACA-Read: Stay-Current Plan for a Cybersecurity Consultant & Auditor (CISA)

**Owner:** info@ocoretech.com
**Created:** 2026-07-07 · **Status:** implemented (see README for operational details)
**Goal:** A repeatable, low-effort system that keeps you current on security news, audit/GRC developments, podcast takeaways, and journal/research content.

---

## 1. What to track (three streams)

### Stream A — News, advisories & daily podcasts → daily digest (6:00 AM IST, weekdays)

| Source | Type | Why it matters |
|---|---|---|
| US CISA (cisa.gov) Alerts & KEV catalog | Advisories | Client risk conversations, audit scoping |
| The Hacker News / BleepingComputer | News | Broad incident coverage |
| Krebs on Security | Blog | Deep incident reporting |
| SANS Internet Storm Center | Daily diary | Practitioner-level threat notes |
| ISACA Now Blog | Blog | Audit/GRC angle |
| Regulatory feeds (SEC cyber rules, EU NIS2/DORA, DPAs) | Regulatory | Directly affects audit criteria |
| SANS Stormcast | Daily podcast | 5-min technical brief |
| Cyber Security Headlines (CISO Series) | Daily podcast | Daily news headlines |

### Stream B — Weekly podcasts → notes (6:30 AM IST, Saturdays)

- **Risky Business** — weekly news analysis
- **CISO Series / Defense in Depth** — governance & leadership (weekly discussion shows)
- **Cloud Security Podcast** — cloud audit relevance
- **ISACA Podcast** — directly CISA-relevant

### Stream C — Journals & research → monthly brief (7:00 AM IST, 1st of month)

- **ISACA Journal** — public TOC/abstracts (member full-text: local sessions only, credentials in local `.env`)
- **NIST publications** (SP 800 series drafts & finals)
- **Verizon DBIR, Mandiant M-Trends, IBM Cost of a Breach** (annual reports, when released)
- **Cloud Security Alliance research**
- Standards watch: COBIT, ISO/IEC 27001/27002, CIS Controls, PCI DSS, SOC 2

---

## 2. How it runs

Fully automated in GitHub Actions (no local machine needed) via one reusable generator; provider-agnostic (Claude OAuth/Sonnet today; Gemini, Cursor, or Copilot by swapping one repo secret). Output is Markdown on the `gh-pages` branch, rendered by GitHub Pages at https://prishs.github.io/isaca-read/; files older than 30 days are removed weekly with squashed history. Prompts (source lists, formats, anti-hallucination and fetch-efficiency rules) live in `prompts/`.

Your part: read the site (or `git fetch origin gh-pages`), and edit prompts/plan on `main` as needs change.

---

## 3. Personal workflow on top of the automation

| Cadence | Activity | Time budget |
|---|---|---|
| Daily (Mon–Fri) | Skim digest; flag 1–3 items relevant to active clients | 10 min |
| Saturday | Read podcast notes + one longer article | 30 min |
| Monthly | Read the brief; pick one NIST/framework item to go deep on | 1–2 hrs |
| Quarterly | Review annual reports (DBIR etc.); refresh personal "audit talking points" | 2 hrs |

---

## 4. Possible future enhancements

- [ ] Client-sector-specific source feeds (add to `prompts/daily-digest.md`)
- [ ] Local monthly deep-dive on ISACA Journal full text using member login (`.env`)
- [ ] Notification (email/push) when a digest lands
