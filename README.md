# isaca-read

A personal stay-current system for a cybersecurity consultant & auditor (CISA).

Every weekday at 7:00 AM, an automated agent sweeps security news sources — US CISA alerts & KEV catalog, The Hacker News, BleepingComputer, Krebs on Security, SANS Internet Storm Center, the ISACA blog, and regulatory feeds — and writes a deduplicated, audit/consulting-relevance-ranked digest to [`digests/`](digests/) as a Markdown file.

## How it works

- **`digests/`** — one Markdown file per weekday (`YYYY-MM-DD.md`), generated automatically.
- **`notes/`** — weekly takeaway notes (podcast summaries, flagged items).
- **`briefs/`** — monthly journal/research one-pagers (ISACA Journal, NIST releases).
- **`PLAN.md`** — the full plan: sources tracked, cadence, and workflow.

## Viewing

The repo is published with **GitHub Pages** (built-in Jekyll), so every Markdown digest renders as a web page. The [index page](index.md) auto-lists the available digests — no manual index maintenance.

## Content generation (provider-agnostic)

Three scheduled GitHub Actions workflows share one reusable generator ([`.github/workflows/generate.yml`](.github/workflows/generate.yml)) — no local machine needed:

| Workflow | Schedule (UTC) | Prompt | Output |
|---|---|---|---|
| [Daily digest](.github/workflows/daily-digest.yml) | Weekdays 05:00 (7 AM Berlin summer) | [`prompts/daily-digest.md`](prompts/daily-digest.md) | `digests/YYYY-MM-DD.md` |
| [Weekly podcast notes](.github/workflows/weekly-notes.yml) | Fridays 05:30 | [`prompts/weekly-notes.md`](prompts/weekly-notes.md) | `notes/YYYY-Www.md` |
| [Monthly journal brief](.github/workflows/monthly-brief.yml) | 1st of month 06:00 | [`prompts/monthly-brief.md`](prompts/monthly-brief.md) | `briefs/YYYY-MM.md` |

The generator picks whichever AI provider secret is configured (Settings → Secrets and variables → Actions), in this priority order:

| Secret | Provider | Cost |
|---|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Claude (subscription, **Sonnet** model) | Included in existing Claude plan — generate with `claude setup-token` |
| `ANTHROPIC_API_KEY` | Claude (API) | Pay per token |
| `GEMINI_API_KEY` | Gemini | Free API tier available |
| `CURSOR_API_KEY` | Cursor | Cursor plan / usage-based |

Add exactly one secret to start; swap providers later by changing secrets — no workflow edits needed. The workflow commits the digest itself, so pull (rather than push) to sync locally.

## Retention

A GitHub Actions workflow ([`.github/workflows/cleanup.yml`](.github/workflows/cleanup.yml)) runs daily and deletes generated files (digests, notes, briefs) older than **30 days**, based on each file's last commit date.
