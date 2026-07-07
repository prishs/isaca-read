# ISACA-Read: Stay-Current Plan for a Cybersecurity Consultant & Auditor (CISA)

**Owner:** info@ocoretech.com
**Created:** 2026-07-07
**Goal:** A repeatable, low-effort system that keeps you current on security news, audit/GRC developments, podcast takeaways, and journal/research content.

---

## 1. What to track (three streams)

### Stream A — News & advisories (daily/weekly)
Fast-moving items: breaches, vulnerabilities, regulatory changes.

| Source | Type | Why it matters for you |
|---|---|---|
| US CISA (cisa.gov) Alerts & KEV catalog | Advisories | Client risk conversations, audit scoping |
| The Hacker News / BleepingComputer | News | Broad incident coverage |
| Krebs on Security | Blog | Deep incident reporting |
| SANS Internet Storm Center | Daily diary | Practitioner-level threat notes |
| ISACA Now Blog & @ISACA newsletter | Blog/newsletter | Audit/GRC angle |
| Regulatory feeds (SEC cyber rules, EU NIS2/DORA, local DPA) | Regulatory | Directly affects audit criteria |

### Stream B — Podcasts (weekly summaries)
Listen or read AI-generated summaries; log takeaways.

- **Risky Business** — weekly news analysis
- **SANS Stormcast** — 5-min daily technical brief
- **CISO Series / Defense in Depth** — governance & leadership angle
- **Cloud Security Podcast** — cloud audit relevance
- **ISACA Podcast** — directly CISA-relevant

### Stream C — Journals & research (monthly/quarterly)
Slower, deeper material.

- **ISACA Journal** (member content — accessible via your isaca.org login)
- **NIST publications** (SP 800 series drafts & finals)
- **Verizon DBIR, Mandiant M-Trends, IBM Cost of a Breach** (annual reports)
- **Cloud Security Alliance research**
- **Academic/industry**: Computers & Security, IEEE S&P highlights (skim abstracts)

---

## 2. Cadence & workflow

| Cadence | Activity | Time budget |
|---|---|---|
| Daily (Mon–Fri) | Skim news digest; flag 1–3 items relevant to active clients | 10 min |
| Weekly (e.g. Friday) | Podcast summaries + one longer article; write 3-bullet takeaways | 30–45 min |
| Monthly | ISACA Journal issue + one NIST/framework update | 1–2 hrs |
| Quarterly | Review annual reports (DBIR etc.); update your personal "audit talking points" doc | 2 hrs |

**Capture format:** one Markdown note per week in this repo (`notes/YYYY-WW.md`) with sections: *News flags*, *Podcast takeaways*, *Journal/research*, *Client-relevant actions*.

---

## 3. How I (Claude Code) can automate this

1. **Scheduled digest agent** — a recurring routine (e.g. weekday mornings) that:
   - Searches/fetches the Stream A sources,
   - Produces a deduplicated digest ranked by relevance to consulting/audit work,
   - Writes it to `digests/YYYY-MM-DD.md` (or sends a notification).
2. **Weekly podcast summary run** — fetch show notes/transcripts for the podcasts above and produce 3-bullet summaries per episode into `notes/`.
3. **Monthly journal sweep** — deep-research pass over new ISACA Journal TOC (using your isaca.org login for member content), NIST releases, and framework changes; output a one-page brief to `briefs/`.

> To activate any of these, just ask me to "set up the schedule" — I'll create the recurring agents.

---

## 4. Repo structure (proposed)

```
isaca-read/
├── PLAN.md            ← this file
├── digests/           ← automated daily/weekly news digests
├── notes/             ← your weekly takeaway notes (YYYY-WW.md)
└── briefs/            ← monthly journal/research one-pagers
```

---

## 5. Next steps

- [ ] Confirm/edit the source lists above (add region-specific regulators, client-sector feeds)
- [ ] Decide delivery: files in this repo, email, or notifications
- [ ] Provide isaca.org login (store in a local `.env` file, kept out of git) for member-only Journal access
- [ ] Ask me to set up the scheduled digest routine
