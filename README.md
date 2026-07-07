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

## Retention

A GitHub Actions workflow ([`.github/workflows/cleanup.yml`](.github/workflows/cleanup.yml)) runs daily and deletes digest files older than **30 days**, keeping the repo lean.
