---
title: isaca-read
---

# Security & Audit Digests

Daily news digests for cybersecurity consulting and audit work. Generated each weekday at 7:00 AM; files older than 30 days are removed automatically.

## Latest digests

{% assign digests = site.pages | where_exp: "p", "p.dir == '/digests/'" | sort: "path" | reverse %}
{% if digests.size > 0 %}
{% for d in digests %}
- [{{ d.name | remove: ".md" | remove: ".html" }}]({{ d.url | relative_url }})
{% endfor %}
{% else %}
_No digests yet — the first one lands on the next weekday morning run._
{% endif %}

## Other sections

- [Weekly notes](notes/) — podcast takeaways and flagged items
- [Monthly briefs](briefs/) — ISACA Journal & research one-pagers
- [Plan](PLAN.md) — sources tracked, cadence, and workflow
