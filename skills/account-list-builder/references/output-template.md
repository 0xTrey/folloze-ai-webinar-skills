# Account list handoff

Return these files or named blocks. Keep the outputs private until reviewed.

## ranked-account-list.csv

Include: account_id, original_row_ids, company_name, domain, relationship_status, disposition, priority_band, score_if_used, criterion_results, confidence, inclusion_reason, risk_or_gap, source_ids, duplicate_of, review_state.

Use one row per resolved company. Keep unresolved identities and original rows in the review file. Quote CSV fields correctly. Do not manufacture domains to complete the table.

## targeting-criteria.md

Record seller scope, Company Brain version, campaign goal, approved source boundary, eligibility rules, exclusions, relationship holds, priority criteria, weights if used, unknown handling, tool-map version/routes, and review owner or proposed reviewer.

## account-list-review.md

- Raw rows and resolved unique companies, with the counting rule.
- Every original row's disposition and retained duplicate target.
- Missing domains, identity conflicts, relationship holds, weak evidence.
- Reasons the top accounts belong and what would change that decision.
- Participant decisions, unresolved questions, and next action.
- Saved location/readback or manual-save state.

## source-register.md

For each consequential claim: source ID, account ID, original URL or record/row, source date, access date, supported criterion, limits, evidence label, and approval/use scope.

Carry the same account IDs into segmentation. Keep proposed fit and priority distinct from a verified relationship or buying signal.
