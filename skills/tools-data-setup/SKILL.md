---
name: tools-data-setup
description: "Create a portable tool map for marketing workflows by identifying participant-owned tools, operations exposed in the current AI workspace, verified access, data scope, contact-enrichment costs, credit limits, and manual alternatives. Run at campaign setup or when the stack changes."
---

# Tools Data Setup

Help a marketer use the tools they already have. Produce `tool-map.md`, a capability-to-workflow guide, and a blank usage ledger. A separate tools chat may build the map; downstream skills need its saved contents, not access to that chat's history.

Read [tool-map-template.md](references/tool-map-template.md) for the output. Read [tool-map-use.md](references/tool-map-use.md) for the shared execution rules and [enrichment-and-limits.md](references/enrichment-and-limits.md) for enrichment and cost handling.

## 1. Ask for the tools they know

Ask one short question: "Which tools do you use for company docs, CRM, contact search or enrichment, engagement or intent, and creative? Name what you know; I’ll check what is available here."

Accept an incomplete list. Ask for the approved AI workspace, data scope, and preferred storage only when needed for the next read or save. Do not require a new subscription, account connection, password, API key, or full-stack inventory to start.

Record owned or licensed tools as participant-reported. This does not prove access from the current AI workspace. Keep unreported tools found in the workspace marked ownership unknown rather than claiming a license.

## 2. Discover actual operations

Inspect the current environment's available tool descriptions, schemas, connection metadata, or documented discovery mechanism. Map exact operations to useful capabilities: document read/write, CRM lookup, company search, people search, current-role check, email enrichment, email verification, engagement, intent, image/design, and destination save.

Use one row per operation, with its provider and actual tool name. A connector can expose a read without exposing export, enrichment, or writes. Public provider documentation may describe features absent from the current workspace; keep those manual-only or unavailable here.

For custom APIs, local tools, and unnamed providers, use their discovered schema and participant-supplied documentation. If introspection is unavailable, mark the operation unverified and provide a manual path. Do not invent an endpoint or infer functionality from a product name.

## 3. Verify access and limits

Check permission scope and operation cost before making a verification call. Prefer a documented nonbillable status, balance, or tightly scoped read. If its cost or permitted data scope is unknown, leave verification pending and request a current provider receipt or approved export.

Record verification separately for each tested operation, with date, safe receipt, scope, and limits. A successful balance lookup does not verify people search; a connection badge does not verify authentication or data access. A failure does not establish that no data exists.

For each enrichment/search operation, record billing basis, credit-pool ID and units, current balance, observation time, source, task allowance, money limit when applicable, and overage state. Keep unknowns unknown. Setup defaults to zero authorized charged operations; building the map is not permission to spend credits.

Do not change credentials, permissions, spending settings, or subscriptions. Continue with manual routes when a connection or cost check is unresolved.

## 4. Route the webinar workflows

Choose routes by needed capability, available access, permitted scope, source quality, and verified cost. Reuse existing CRM contacts and approved exports before proposing new discovery or enrichment.

Map Company Brain to docs/research/storage; segmentation to account evidence; account briefs to CRM/research/engagement/intent; buyer groups to contacts/current-role/enrichment/verification; creative to approved assets/image/design; email copy to context and optional link checks. Mail sending, ad launch, and CRM writes need separate authorization.

For every missing route, give a precise manual request, required fields, source date, identity keys, and export limits. A participant can use their existing UI and upload an approved CSV or excerpt. Never claim a manual operation ran until the result is supplied and checked.

## 5. Save and maintain the map

Return named Markdown/CSV files in the participant's chosen authorized location, or named content blocks for manual saving. Include a compact readiness table, unverified operations, manual alternatives, and next actions.

Ask the participant to confirm permitted data use and any proposed task allowance. Reuse existing approval within its exact scope. Keep an unapproved allowance pending; do not treat silence as approval.

Attach the map with the Company Brain and relevant outputs when invoking another skill. Each skill must check the route against its current workspace before execution and refresh balances before charged work. Refresh the map after tool, scope, price, or permission changes. Finish with actual save/readback and verification states; stop after setup unless further operations are explicitly authorized.
