---
name: campaign-segmentation
description: "Segment an attendee-supplied account list into explainable one-to-few campaign cohorts using seller ICP, account evidence, and a shared buying problem. Return assignments, exceptions, and campaign angles without sourcing a new list or activating outreach."
---

# Campaign Segmentation

Turn an existing account list into useful campaign groups. Group accounts by a problem the seller can address, rather than industry labels alone.

Read [context-and-evidence.md](references/context-and-evidence.md) for seller context, evidence labels, storage, and handoff rules. Use [output-template.md](references/output-template.md) for the deliverables.

Read [tool-map-use.md](references/tool-map-use.md). Use `tool-map.md` for account lookup, company research, and export/storage routes; record its version and selected route IDs. Reuse the supplied list and CRM evidence before proposing new queries. Keep cost or access gaps on the review queue and use manual exports when needed.

## 1. Start from the supplied list

Ask only for the list and seller context if missing. Use the Company Brain's ICP, product positioning, messaging, and personas, or accept an approved summary of those areas. Default the goal to a reviewable one-to-few campaign hypothesis when no campaign goal is supplied.

Preserve participant-provided account IDs, domains, existing groups, suppressions, relationship holds, and required regions. Normalize names and domain casing for comparison, but do not silently merge subsidiaries or different legal entities. Missing identity and duplicate candidates go to review with their original row references.

## 2. Check fit and exceptions

Apply explicit exclusions and holds before grouping. High fit cannot override a disqualifier. Check each relevant ICP criterion against supplied facts or permitted primary company sources; mark unsupported criteria Missing.

If public research is available, focus on the missing fact needed for the grouping decision. If browsing or a CRM connection is unavailable, continue from the list and note the coverage limit. Do not source net-new accounts, enrich people, or assume customer/opportunity status.

Respect the participant's relationship rules. Flag an existing customer, open opportunity, or relationship unknown for the appropriate campaign decision; do not invent a universal exclusion rule. Fit is not intent or permission to contact.

## 3. Define the cohorts

Propose a small set of cohorts based on shared use case, problem, operating context, or buying motion. Use industry as supporting context when it changes the message. Give each cohort a stable ID, entry rule, exclusion rule, evidence needed, and a distinct campaign premise.

Show why each account belongs. Use one primary cohort per included account and optional secondary tags. Add a review group when evidence or identity is insufficient; do not force every account into a marketable segment.

Keep rules understandable without a hidden score. If the participant requests scoring, expose the definitions and unknowns rather than adding arbitrary weights.

## 4. Build the campaign handoff

Return cohort rules, account assignments, a review queue, and source coverage. For each cohort, propose a problem, buyer-group hypothesis from the seller personas, relevant product capability, approved proof or proof gap, and one draft CTA.

Keep account IDs and segment IDs for Account Brief Builder and Buyer Group Mapper. Separate the seller's approved ICP rules from inferred account needs. A shared campaign premise is a test hypothesis until reviewed.

## 5. Review and reconcile

Account for every original row as Included, Review, Held, Excluded, or Duplicate. Report unique accounts separately from raw rows, and document the duplicate target instead of discarding it. Check that each included account has exactly one primary cohort.

Show any cohort that lacks a common problem or usable seller relevance. Ask the participant to review the cohort definitions and exceptions; record review pending if no answer arrives. Finish with the group counts, coverage limits, top decisions, and saved or returned-file state. Stop before activation.
