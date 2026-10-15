# Use the participant's tool map

Read the supplied `tool-map.md` before selecting data, research, enrichment, creative, or storage operations. Record its ID/version and the route IDs used in the output's review notes. The map is participant context; it is not bundled inside a skill and does not require access to another chat.

## Choose a route

Match the needed capability to an exact operation exposed in this workspace. Keep ownership, availability, tested access, allowed data scope, and cost separate. A mapped operation from another AI tool or an older session is not automatically executable here.

Inspect the current schema and connection evidence. Refresh stale access using a known nonbillable, scoped check. A successful balance read verifies that read only. Do not call an operation with unknown charge or permission merely to test it.

Prefer participant-designated source precedence and existing approved data. Reuse CRM contacts and prior verified observations before net-new discovery or enrichment. Keep every result's source, dates, reporting coverage, identity evidence, and limits. Tool access does not establish source truth or claim approval.

If the map is absent, do not block useful draft work. Make a small provisional table for the capabilities this task needs: exact exposed operation or manual source, access state, permitted scope, cost known/unknown, and fallback. Default authorized charged usage to zero. Ask only for the missing tool, scope, or allowance that changes the next action. Tools & Data Setup can create a fuller map when available.

## Charged operations, including contact enrichment

A tool-map entry or available subscription balance is not permission to spend. Before a potentially charged query, page, search, reveal, enrichment, verification, retry, or image operation, require all of the following:

- The actual operation is exposed, its scoped access verified, and current billing trigger and worst-case cost known from reliable provider evidence.
- Explicit participant authorization covers the task, accounts/groups, fields, provider operations, credit pool, maximum records, and credit/money limits when applicable. Reuse prior approval within that exact scope; otherwise return the bounded plan for approval.
- A fresh provider balance and shared ledger establish remaining task and pool capacity after spent and outstanding reservations. Never combine different pools, credit units, or currencies. Resolve concurrent usage through the existing shared reservation authority or use the manual route.
- The next bounded call fits all applicable provider, task, record, rate, and money limits, including pagination, dependent reveals, verification, and failure charges. Unknown overage behavior, balance, maximum debit, or unbounded follow-on work makes the automatic route held.
- The worst-case amount is reserved before the call. Execute small serial batches and reconcile actual debit and result evidence before continuing.

Retain the full reservation after an ambiguous timeout or unconfirmed debit; mark `outcome_unknown` and stop related operations in that pool until reconciled. No blind retry, alternate-provider retry, or free-failure assumption. If actual debit exceeds the bound, stop charged use of that pool and resolve it.

Record safe call IDs, scope references, approval, balances, reservation, debit, time, result, and state in the participant's shared usage ledger. Do not imply a provider hard cap from a local ledger or instructions. Do not buy credits, enable overage, change billing, or import into a CRM to make the route work.

Contact enrichment results must separate current company/role, role relevance, email verification, buying authority, and communication eligibility. Only request needed professional fields. An email result does not prove all of these, and successful verification does not authorize sending.

## Manual fallbacks and stopping points

For owned but disconnected tools, give exact account/domain and role filters, needed fields, exclusions, date/period, and a count ceiling. The participant checks the operation's cost and approved allowance, runs it in their existing tool, and uploads an approved export. Do not claim execution, debit, connection verification, or complete coverage from a planned export.

For missing CRM, engagement, or intent access, request a scoped export with original record IDs, event types, reporting window, and completeness. Missing access is not zero activity. For docs, use approved files or excerpts. For creative, use a build brief if generation is unavailable or unapproved. For storage, return named files or Markdown blocks for manual saving in Drive, OneDrive, or a local folder.

An unknown-cost or unapproved route remains held while draft work continues from available sources. Respect a platform refusal; do not reroute to bypass it. Keep colleagues' messages, account connections, permission changes, CRM writes, publication, ad launch, enrollment, and sending outside this workflow unless separately authorized.

## Optional arithmetic check

When Python is available, use the bundled [check_tool_budget.py](../scripts/check_tool_budget.py) with a documented next-call snapshot. It checks separate provider, pool, and task limits per `pool|unit` dimension, readiness flags, and unresolved outcomes. It makes no provider call or reservation and cannot grant permission or enforce provider billing. Follow the rules above before execution; otherwise keep the route manual. The snapshot schema is available from Tools & Data Setup, or inspect this self-contained script to construct it.
