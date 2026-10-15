# Engagement and follow-up handoff

## engagement-summary.md

Record campaign/board, period/timezone, source files or exact read operations, retrieval time, filters, tool-map version/routes, coverage, and review state.

Define the counting units and attribution model. Reconcile raw rows, duplicates, retained events, known people, accounts, suspected automation, and unknown classification. Counts may have different denominators; do not force them to match one another.

Report supported content and channel findings with source IDs and limits. Registration attribution needs registration events and relevant fields. Keep unavailable measures Missing.

## engagement-signals.csv

Include: signal_id, source_file, source_row_or_record_ids, period, identity_type, person_id_if_verified, account_id_if_supported, content_id, observed_event, event_count, metric_unit, recorded_utms, automation_state, coverage_limit, interpretation, review_state.

Keep interpretations distinct from observations. Avoid including raw private contact data when IDs suffice.

## sales-follow-up.md

For each proposed action: signal IDs, person or account scope, buyer context, relationship rule, confirmed or suggested owner, useful topic/resource, unsent draft, holds, and next review decision.

Do not attribute anonymous account activity to an individual. Separate the report, draft, approved action, attempted send, and delivery states.

## source-and-metric-register.md

List source locations, record references, event definitions, timezone, period, duplicate rule, identity mapping, conversion rule, attribution model, automation rule, missing fields, and reconciliation checks.

End with one measurable next test, a suggested owner, and the evidence needed to judge it. Do not invent a performance baseline.
