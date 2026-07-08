# isaca-read

A personal stay-current system for a cybersecurity consultant & auditor (CISA).

Every weekday morning an automated agent sweeps security news sources — US CISA alerts & KEV catalog, The Hacker News, BleepingComputer, Krebs on Security, SANS Internet Storm Center, the ISACA blog, regulatory feeds — plus the daily podcasts (SANS Stormcast, Cyber Security Headlines) and publishes a relevance-ranked Markdown digest. Weekly podcast notes land on Fridays and a journal/research brief on the 1st of each month.

## Branch layout

- **`main`** — source only: prompts, workflows, this README, [`PLAN.md`](PLAN.md). Human-edited, pushed manually.
- **`gh-pages`** — generated content only: `digests/YYYY-MM-DD.md`, `notes/YYYY-Www.md`, `briefs/YYYY-MM.md`, plus the Jekyll config and auto-listing index. Written exclusively by the workflows and served by GitHub Pages. Its history is squashed to a single snapshot commit by the weekly cleanup, so removed files don't linger in git history.

## Content generation (provider-agnostic)

Three scheduled GitHub Actions workflows share one reusable generator ([`.github/workflows/generate.yml`](.github/workflows/generate.yml)) — no local machine needed:

| Workflow | Schedule (UTC) | Prompt | Output (on `gh-pages`) |
|---|---|---|---|
| [Daily digest](.github/workflows/daily-digest.yml) | Weekdays 00:30 (6:00 AM IST) | RSS pre-fetch → research → write (see [Daily digest pipeline](#daily-digest-pipeline)) | `digests/YYYY-MM-DD.md` |
| [Weekly podcast notes](.github/workflows/weekly-notes.yml) | Saturdays 01:00 (6:30 AM IST) | [`prompts/weekly-notes.md`](prompts/weekly-notes.md) | `notes/YYYY-Www.md` |
| [Monthly journal brief](.github/workflows/monthly-brief.yml) | 1st of month 01:30 (7:00 AM IST) | [`prompts/monthly-brief.md`](prompts/monthly-brief.md) | `briefs/YYYY-MM.md` |

The generator picks whichever AI provider secret is configured (Settings → Secrets and variables → Actions), in this priority order:

| Secret | Provider | Cost |
|---|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | Claude (subscription; daily digest uses **Haiku** for research + **Sonnet** for write) | Included in existing Claude plan — generate with `claude setup-token` |
| `ANTHROPIC_API_KEY` | Claude (API) | Pay per token |
| `GEMINI_API_KEY` | Gemini | Free API tier available |
| `CURSOR_API_KEY` | Cursor | Cursor plan / usage-based |
| `COPILOT_GITHUB_TOKEN` | GitHub Copilot | Copilot plan; Free tier's ~50 premium requests/month is tight for ~27 runs — fine-grained PAT with "Copilot Requests" permission |

Add exactly one secret to start; swap providers later by changing secrets — no workflow edits needed.

### Daily digest pipeline

All providers get the same **RSS/KEV pre-fetch** step (`scripts/fetch-digest-sources.py` → `/tmp/digest-prefetch.md`):

| Pre-fetched (CI, no tokens) | Agent research (web fetch) |
|---|---|
| CISA advisories RSS | **Cyber Security Headlines** (no public RSS from CI) |
| CISA KEV JSON | **ISACA Now blog** (RSS blocked / 403 from GitHub Actions) |
| The Hacker News | Regulatory watch (SEC, NIS2/DORA) when not in prefetch |
| BleepingComputer | |
| Krebs on Security | |
| SANS ISC diaries + Stormcast | |

**Claude** (`CLAUDE_CODE_OAUTH_TOKEN` or `ANTHROPIC_API_KEY`): two-phase — **Haiku** research (`daily-digest-research.md`, fills the agent column above) → **Sonnet** write (`daily-digest.md`, no web tools).

**Gemini, Cursor, Copilot**: no Haiku/Sonnet split — one **combined** run (`daily-digest-combined.md`) that reads the prefetch file, does the gap-filling web research, and writes the digest in a single session. RSS pre-fetch still runs; only the model split is Claude-specific.

## Viewing

**GitHub Pages** serves the `gh-pages` branch (Settings → Pages → deploy from branch `gh-pages`, root). Every Markdown file renders as a web page; the index auto-lists digests, notes, and briefs.

## Retention

[`.github/workflows/cleanup.yml`](.github/workflows/cleanup.yml) runs weekly (Sundays) on `gh-pages`: it deletes generated files older than **30 days** (age read from the filename) and force-pushes the branch as a fresh single-commit snapshot, so old content is removed from history, not just from the tree.
