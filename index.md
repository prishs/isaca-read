---
title: isaca-read
---

# Security & Audit Digests

Automated reading pipeline for cybersecurity consulting and audit work. Daily digests each weekday morning, podcast notes on Fridays, a research brief on the 1st of the month. Files older than 30 days are removed automatically.

## Daily digests

{% assign digests = site.pages | where_exp: "p", "p.dir == '/digests/'" | sort: "path" | reverse %}
{% if digests.size > 0 %}
{% for d in digests %}
- [{{ d.name | remove: ".md" | remove: ".html" }}]({{ d.url | relative_url }})
{% endfor %}
{% else %}
_No digests yet — the first one lands on the next weekday morning run._
{% endif %}

## Weekly podcast notes

{% assign notes = site.pages | where_exp: "p", "p.dir == '/notes/'" | sort: "path" | reverse %}
{% if notes.size > 0 %}
{% for n in notes %}
- [{{ n.name | remove: ".md" | remove: ".html" }}]({{ n.url | relative_url }})
{% endfor %}
{% else %}
_No notes yet — generated on Fridays._
{% endif %}

## Monthly briefs

{% assign briefs = site.pages | where_exp: "p", "p.dir == '/briefs/'" | sort: "path" | reverse %}
{% if briefs.size > 0 %}
{% for b in briefs %}
- [{{ b.name | remove: ".md" | remove: ".html" }}]({{ b.url | relative_url }})
{% endfor %}
{% else %}
_No briefs yet — generated on the 1st of each month._
{% endif %}

---

[Plan](PLAN.md) — sources tracked, cadence, and workflow
