# Contact enrichment and limits

Use this procedure when a downstream task requests contact discovery or enrichment. Tools & Data Setup itself discovers routes and costs; it does not spend credits to populate a contact list.

## Choose the smallest useful operation

Reuse existing contacts, approved exports, and prior verified observations first. Normalize account identity and deduplicate professional candidates; preserve historical employer episodes separately from current affiliation.

Only request the missing fields needed for the role map. Company discovery, people discovery, current-role validation, email reveal, and email verification are different operations and may have different charges. A provider email result does not independently verify current employment, buying authority, or communication eligibility.

Agree on account/group scope, excluded records, maximum contacts, fields, provider operations, credit pools, money limits when applicable, and approval expiry. Existing approval is reusable within those limits. A map's capability row, remaining subscription balance, or generic request to map roles is not authorization for charged enrichment.

## Bound each call

Before any potentially charged operation:

- Inspect the actual operation schema and current charge model. Reads, searches, pages, returned matches, reveals, verification, retries, and failures may incur charges.
- Refresh the provider balance and all task/pool reservations. Treat unknown balance, billing basis, overage behavior, or maximum charge as held for automatic execution. Use a manual plan while the participant verifies it.
- Calculate a conservative upper bound including page/result limits and dependent charge triggers. Stop when an unbounded response or asynchronous follow-on work prevents a reliable bound.
- Use the lowest remaining applicable allowance: provider availability minus outstanding reservations, approved pool allowance minus spent and reserved, task allowance minus spent and reserved, and record/call/rate limits. Apply money caps independently; never convert units or currencies using a guessed rate.
- Record the planned scope and reserve the upper bound in the shared pool ledger before execution. Use serial small batches. If another workflow shares the pool, use its existing reservation authority or stop until usage can be coordinated. Do not invent a second independent balance.

Execute only an operation whose access and permitted scope are verified in the current workspace. Refresh stale verification with a known nonbillable check; do not use a paid probe to establish readiness. Do not activate overage, buy credits, or change billing settings.

## Reconcile before continuing

Record actual debit or a trustworthy provider billing receipt, result reference, and balance readback. Balance differences alone may reflect another workflow; retain uncertainty if attribution is unclear. Release only the confirmed unused reservation.

For an ambiguous timeout, interrupted call, or missing debit, retain the full reservation and mark `outcome_unknown`. Stop this route and reconcile the original request before any retry, pagination, fallback provider, or related operation sharing the same pool. Failed calls and partial results are not assumed free.

If actual cost exceeds the bound, pause charged operations in that pool and resolve the discrepancy. Other work can continue from existing approved data. Never claim a provider hard spending cap from a local ledger or prose instruction.

## Use the result carefully

Save field-level source, provider, observation time, identity match, current-employment evidence, and verification outcome. Mark catch-all, unknown, conflicting, or expired email results as such. A deliverability check does not authorize a send.

Return the enriched candidates, remaining field gaps, and usage receipt in the approved private workspace. Stop before CRM import, email sending, enrollment, or colleague communication unless separately requested.

## Manual routes

If the provider is owned but disconnected, supply the exact account/domain and role filters, requested fields, exclusions, and count ceiling. Ask the participant to verify cost and available allowance in their provider UI, perform the authorized bounded export, then upload its approved CSV.

If cost is unknown, ask for the provider's current cost/balance receipt before execution; provide role-level maps and export instructions meanwhile. If no provider exists, return role coverage, known public evidence, and precise sourcing requests. Do not recommend buying a service merely to finish the map.

An uploaded CSV supports local analysis. It does not prove that this assistant verified the connection, performed enrichment, observed the debit, or refreshed every candidate's employment.
