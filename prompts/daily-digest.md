# Daily Security & Audit Digest — Agent Instructions

You are generating today's cybersecurity news digest for a cybersecurity consultant and auditor (CISA-certified). Today's date is **{{DATE}}**.

## Task

Research the past 24–48 hours of security news using web search/fetch, then write a single Markdown file at `digests/{{DATE}}.md`. Do not modify any other files.

## Sources to sweep

- US CISA: new alerts, advisories, and Known Exploited Vulnerabilities (KEV) catalog additions
- The Hacker News, BleepingComputer — major incidents and vulnerabilities
- Krebs on Security — investigative pieces
- SANS Internet Storm Center — daily diary highlights
- ISACA Now blog — audit/GRC items
- Regulatory news: SEC cyber disclosure, EU NIS2/DORA, major data-protection rulings

## Selection & ranking

Pick the 5–10 most relevant items. Rank by relevance to **consulting and IT audit work**: actively exploited vulnerabilities, breaches with control-failure lessons, regulatory changes, and framework/standard updates rank highest; generic product news ranks lowest. Deduplicate stories covered by multiple outlets — one entry, best source linked.

## Output format for `digests/{{DATE}}.md`

```markdown
---
title: "Digest {{DATE}}"
---

# Security & Audit Digest — {{DATE}}

## Top items

### 1. <Headline>
**Why it matters for audit/consulting:** <1–2 sentences>
<2–3 sentence summary> ([source](url))

### 2. ...

## Quick hits
- <one-liner> ([source](url))
- ...

## Regulatory & framework watch
- <item or "Nothing new today">
```

## Rules

- Every item must have a real, working source link you actually found — never invent URLs or stories.
- If research tools fail entirely, still write the file with a note: "Digest generation failed — sources unreachable."
- Keep the whole digest under ~600 words. Plain, direct language.
