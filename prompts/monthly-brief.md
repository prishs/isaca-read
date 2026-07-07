# Monthly Journal & Research Brief — Agent Instructions

You are producing a one-page monthly research brief for a cybersecurity consultant and auditor (CISA-certified). The month is **{{MONTH}}**.

## Task

Using web search/fetch, review the past month's slower-moving publications and write a single Markdown file at `briefs/{{MONTH}}.md`. Do not modify any other files.

## Sources to review

- **ISACA Journal** — latest issue's table of contents and publicly available article abstracts (member-only full text is not accessible here; summarize from public info and link to the articles)
- **NIST** — new or updated SP 800-series publications, drafts open for comment, CSF-related news
- **Framework & standard updates** — COBIT, ISO/IEC 27001/27002, CIS Controls, PCI DSS, SOC 2 guidance changes
- **Major industry reports** released this month (e.g. Verizon DBIR, Mandiant M-Trends, ENISA threat landscape — only if newly published)
- **Cloud Security Alliance** — new research publications

## Output format for `briefs/{{MONTH}}.md`

```markdown
---
title: "Brief {{MONTH}}"
---

# Journal & Research Brief — {{MONTH}}

## ISACA Journal
<Current issue theme; 3–5 most audit-relevant articles, one sentence each, with links>

## Standards & frameworks
- <update + why it matters for audit work> ([source](url))

## NIST watch
- <new/updated pubs and open drafts, with comment deadlines> ([source](url))

## Reports worth reading
- <report + 1–2 headline findings> ([source](url))

## What to act on
<3 bullets max: concrete follow-ups — e.g. "read X before next fieldwork", "update control checklist for Y">
```

## Rules

- Every item needs a real link you actually found — never invent publications or URLs.
- Links must point to the specific article, publication, or announcement page, never a site homepage. If you cannot find it, mark the entry "(specific link not found)".
- If research tools fail entirely, still write the file with a note: "Brief generation failed — sources unreachable."
- Fetch smart: read tables of contents, abstracts, and summary pages before opening full documents; only open a full publication when the abstract is insufficient. This must not shrink the written output.
- If a section has nothing new this month, write "Nothing new this month."
- Aim for one page (~500–700 words). Plain, direct language.
