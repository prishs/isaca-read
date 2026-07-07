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

## Digest generation (provider-agnostic)

[`.github/workflows/daily-digest.yml`](.github/workflows/daily-digest.yml) runs weekdays at 05:00 UTC (7:00 AM Berlin in summer) entirely in GitHub Actions — no local machine needed. The agent prompt lives in [`prompts/daily-digest.md`](prompts/daily-digest.md).

The workflow picks whichever AI provider secret is configured (Settings → Secrets and variables → Actions), in this priority order:

| Secret | Provider | Cost |
|---|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Claude (subscription) | Included in existing Claude plan — generate with `claude setup-token` |
| `ANTHROPIC_API_KEY` | Claude (API) | Pay per token |
| `GEMINI_API_KEY` | Gemini | Free API tier available |
| `CURSOR_API_KEY` | Cursor | Cursor plan / usage-based |

Add exactly one secret to start; swap providers later by changing secrets — no workflow edits needed. The workflow commits the digest itself, so pull (rather than push) to sync locally.

## Retention

A GitHub Actions workflow ([`.github/workflows/cleanup.yml`](.github/workflows/cleanup.yml)) runs daily and deletes digest files older than **30 days**, keeping the repo lean.
