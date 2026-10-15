# Segmentation output template

Return `campaign-segments.md`, `account-segments.csv` or a Markdown table, and `segmentation-review.md`. The CSV is optional; ordinary Markdown works when file tools are unavailable.

## campaign-segments.md

- Seller/product, Company Brain version, campaign goal, scope, as-of date
- Source boundary, participant exclusions and relationship rules
- Tool-map ID/version, used route IDs, access/coverage state, and manual alternatives
- Review state and owner

| Segment ID | Name | Shared problem | Entry/exclusion rule | Evidence needed | Campaign premise | Buyer-group hypothesis | Capability | Approved proof or gap | Draft CTA |
|---|---|---|---|---|---|---|---|---|---|
| SEG-1 | {name} | {problem} | {rule} | {fields} | {draft premise} | {persona reference} | {approved seller capability} | {proof ID or Missing} | {action} |

## account-segments.csv or table

| Original row ID | Account ID | Company/domain | Primary segment ID | Disposition | Reason for assignment or exception | ICP evidence/unknowns | Source IDs | Evidence | Approval | Secondary tags |
|---|---|---|---|---|---|---|---|---|---|---|
| {row} | {stable ID} | {identity} | {segment or blank} | {Included, Review, Held, Excluded, Duplicate} | {specific reason; duplicate target if relevant} | {criterion findings} | {sources} | {label} | {label} | {optional} |

Duplicate rows retain their row ID and point to the surviving account. Conflicting duplicate fields remain a review issue. Do not assign a held or excluded account to an active cohort.

## segmentation-review.md

- Raw row count and reconciled disposition counts
- Unique-account count and duplicate handling
- Each primary cohort's included-account count
- Source register with locators, source dates, access dates, and missing coverage
- Identity conflicts, fit gaps, and relationship decisions
- Participant corrections, review owner, state, and next action
- Handoff: segment rules and stable IDs for briefs and buyer-group mapping
- Local creation, storage readback, and activation state separately
