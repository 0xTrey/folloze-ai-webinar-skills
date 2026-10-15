---
name: follow-up-measurement
description: "Analyze actual campaign engagement from Folloze or supplied exports, reconcile people, accounts, events, and attribution, and prepare source-backed sales follow-up drafts. Use for post-visit analysis and next-action planning, not automatic sending or intent claims."
---

# Engagement & Follow-up

Turn observed engagement into a useful next action. Work from the participant's actual data, not an assumed integration.

Read [context-and-evidence.md](references/context-and-evidence.md), [tool-map-use.md](references/tool-map-use.md), and [output-template.md](references/output-template.md). A CSV export and seller summary are enough to start.

## 1. Establish the reporting scope

Confirm the board or campaign, date range, timezone, and business question. Inventory available exports or authorized read-only analytics routes. Map actual columns to event time, event type, record ID, person/contact identity, account identity, content, source/medium/campaign/creative, and any conversion fields.

Record filters, field meanings, source windows, and missing coverage. If a necessary field is absent, report the limit and continue with supported questions. Never infer complete coverage or zero activity from missing access.

## 2. Reconcile events and identities

Preserve original rows and source IDs. Deduplicate exact event IDs when available. Otherwise document a conservative duplicate rule and retain ambiguous collisions for review; do not merge real repeat visits just because the person and content match.

Count raw rows, retained events, visits, known people, and accounts separately. Apply only evidenced account mappings. Keep anonymous account activity, identified contacts, and unknown identities distinct. A company identification does not identify the visitor.

Flag suspected automation only when evidence supports it, and explain the rule. Retain Unknown when it does not. Email opens, platform clicks, board visits, content engagement, registrations, attendance, replies, and opportunities are different events.

## 3. Explain what happened

Report content explored, repeat visits, time, and meaningful actions only where the source supports those measures. Define units and denominators. Do not add average durations, mix incompatible windows, or present missing values as zero.

For source attribution, state the conversion definition and supported attribution rule. Use an existing documented model when supplied; otherwise offer a descriptive breakdown using recorded conversion-row UTMs, with Unknown kept visible. Do not claim who drove registrations from visit-only data or silently assign missing UTMs to LinkedIn, email, or direct traffic.

Attach source row/record IDs to the useful signals. Separate observed facts, interpretation, and a proposed action. Visits are not proof of buying intent, pipeline, or human attention.

## 4. Prepare useful follow-up

Use the account brief, buyer role, relationship rules, and approved content to propose one next action per supported person or account. For anonymous activity, keep the recommendation account-level and do not assign it to a known employee.

Return a suggested owner, topic, evidence basis, useful next resource, and holds. Draft a concise email, LinkedIn message, or phone opener when requested. Avoid claiming to have watched someone's activity. Use Buyer Group Email Copy when installed; otherwise draft from the approved seller context without requiring another skill.

Keep all messages unsent. Do not enrich people, enroll a cadence, write CRM records, or expose private visitor information in public creative.

## 5. Review and hand off

Reconcile totals to the source scope and show exclusions, suspected automation, identity gaps, and attribution limits. Include the metric definitions and one proposed follow-up test with no invented baseline.

Return the report, signal table, and follow-up drafts with review state, source register, and next actions. Ask for review before activation. Saving a report does not establish delivery, sales acceptance, or campaign results.
