# Daily Security & Audit Digest — Write Phase (Sonnet)

You are writing today's cybersecurity news digest for a CISO, VAPT Specialist, CISA-Certified IS/IT Auditor. Today's date is **{{DATE}}**.

## Task

Write a single Markdown file at **`digests/{{DATE}}.md`** using **only** the pre-researched material below. Do **not** use WebSearch or WebFetch. Do not modify any other files.

## Inputs (read all before writing)

1. **`/tmp/digest-prefetch.md`** — RSS + CISA KEV candidates (primary list)
2. **`/tmp/digest-research.md`** — research agent brief (ranked items, podcasts, regulatory)
3. **Previous digest** (if appended below) — for deduplication only; do not repeat items unless research notes **new** reporting since {{CUTOFF_DATE}}

If research and prefetch disagree on dates, **drop the item** (when in doubt, exclude).

## Recency gate (hard rule — never violate)

**Include an item only if its triggering event is dated on or after {{CUTOFF_DATE}}.**

Exclude anything older, evergreen framework background, or stories already in the previous digest without new reporting in the window.

**Regulatory & framework watch:** Only concrete new activity since {{CUTOFF_DATE}}. If nothing qualifies, write exactly: `Nothing new in the past 3 days.`

**Podcast briefings:** Only episodes released on or after {{CUTOFF_DATE}}.

## Selection & ranking

Pick the 5–10 most relevant items from the inputs. Rank by relevance to **IS/IT audit, CISO, and VAPT work**:
1. **Highest:** actively exploited vulnerabilities, breaches with control-failure lessons, regulatory changes, framework/standard updates (audit)
2. **High:** security-program or board-level impact (CISO)
3. **High:** new public PoCs/exploits, attack techniques, notable vulnerability write-ups (VAPT)
4. **Lowest:** generic product news

Deduplicate across outlets — one entry, best source linked.

## Output format for `digests/{{DATE}}.md`

```markdown
---
title: "Digest {{DATE}}"
---

# Security & Audit Digest — {{DATE}}

## Top items

### 1. <Headline>
**Why it matters for audit/CISO/VAPT:** <1–2 sentences>
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
- <item dated on or after {{CUTOFF_DATE}}, or exactly "Nothing new in the past 3 days.">
```

In podcast sections, cross-reference Top items instead of repeating full summaries ("covered in item 2 above" is fine).

## Rules

- Every item must have a real source link from the input files — never invent URLs or stories.
- Every item must fall within the recency gate; when in doubt, drop it.
- Links must point to the specific article or episode page, never a site homepage.
- If inputs are empty or unusable, write the file with: "Digest generation failed — sources unreachable."
- Keep the whole digest under ~800 words. Plain, direct language.
