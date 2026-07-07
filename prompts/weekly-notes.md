# Weekly Podcast Notes — Agent Instructions

You are producing this week's podcast takeaways for a CISO, VAPT Specialist, CISA-Certified IS/IT Auditor. Today's date is **{{DATE}}**; this is week **{{WEEK}}**.

## Task

Using web search/fetch, find the episodes published in the last 7 days for the podcasts below, read their show notes (and transcripts where freely available), and write a single Markdown file at `notes/{{WEEK}}.md`. Do not modify any other files.

## Podcasts to cover

Start from these sites (fall back to web search only if a page is unreachable or moved):

- **Risky Business** (risky.biz) — weekly news analysis
- **CISO Series / Defense in Depth** (cisoseries.com) — governance & leadership (the weekly discussion shows, not the daily Cyber Security Headlines — that's covered in the daily digest, as is SANS Stormcast)
- **Cloud Security Podcast** (cloudsecuritypodcast.tv) — cloud security & audit
- **ISACA Podcast** (isaca.org/resources/news-and-trends/isaca-podcast-library) — audit/GRC

## Output format for `notes/{{WEEK}}.md`

```markdown
---
title: "Podcast notes {{WEEK}}"
---

# Podcast Notes — Week {{WEEK}}

## Risky Business — <episode title> (<date>)
- <takeaway 1>
- <takeaway 2>
- <takeaway 3>

[Episode link](url)

(one section per show; 3 bullets each)

## Audit, CISO & VAPT angle
<2–4 sentences: which of this week's themes are worth raising with audit clients, bringing to leadership/board discussions, or factoring into VAPT engagements, and why>
```

## Rules

- Only include episodes that actually exist, with real links you found — never invent episodes or URLs.
- Links must point to the specific episode page, never a show homepage. If you cannot find it, mark the entry "(specific link not found)".
- If research tools fail entirely, still write the file with a note: "Notes generation failed — sources unreachable."
- Fetch smart: prefer show notes and episode descriptions over full transcripts; only open a transcript if the notes are too thin. This must not shrink the written output.
- If a show published nothing this week, write "No new episode this week." under its heading.
- Takeaways should be substantive (what was said and why it matters), not descriptions of the episode topic.
- Keep the whole file under ~800 words.
