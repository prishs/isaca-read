# Daily Security & Audit Digest — Combined Run

You are generating today's cybersecurity news digest for a CISO, VAPT Specialist, CISA-Certified IS/IT Auditor. Today's date is **{{DATE}}**.

## Task

1. Read **`/tmp/digest-prefetch.md`** (RSS + KEV candidates pre-fetched in CI).
2. Fill gaps with WebSearch/WebFetch only where prefetch is incomplete — **Cyber Security Headlines**, **ISACA Now blog** (not in RSS prefetch), and regulatory items not already covered.
3. Write a single Markdown file at **`digests/{{DATE}}.md`**. Do not modify any other files.

## Recency gate (hard rule)

Include an item only if its triggering event is on or after **{{CUTOFF_DATE}}**. Exclude older items even if relevant.

**Regulatory & framework watch:** Only new activity since {{CUTOFF_DATE}}, or exactly: `Nothing new in the past 3 days.`

**Podcast briefings:** Only episodes released on or after {{CUTOFF_DATE}}.

## Research efficiency

- Start from prefetch; do not re-fetch those RSS sources unless a URL is broken.
- **Hard caps:** at most **8 WebFetch** and **4 WebSearch** calls total.
- Fetch show-notes pages only; no full transcripts.

## Selection, format, and rules

Follow the same ranking, output format, and link rules as the write-phase digest prompt (`prompts/daily-digest.md` in the repo): 5–10 top items, quick hits, two podcast sections, regulatory watch, ~800 words, specific article URLs only.

If a **Previous digest** section is appended below, do not repeat items unless there is new reporting since {{CUTOFF_DATE}}.
