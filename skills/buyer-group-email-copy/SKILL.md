---
name: buyer-group-email-copy
description: "Draft B2B sales emails using value subjects, problem or customer-story openings, role relevance, fixed approved pitches and content CTAs. Prepare AgentMail or Smartlead handoffs from company context and buyer groups, without sending or enrolling contacts."
---

# Buyer Group Email Copy

Turn company context and buyer roles into reviewable sales emails. The same writing framework works with AgentMail, Smartlead or another sender. This skill runs in the AI workspace; it does not install inside an email platform.

Read [context-and-evidence.md](references/context-and-evidence.md). Use [messaging-framework.md](references/messaging-framework.md) for the five sections and role choices, then [output-template.md](references/output-template.md) for the handoff.

Start with supplied files. When connected research or storage is needed, read [tool-map-use.md](references/tool-map-use.md) and the participant's map. Drafting needs no contact enrichment or sending operation.

## 1. Read the message context

Use the Company Brain's voice, personas, product limits, approved pitches and proof. Add the account brief, buyer map, content catalog and campaign destination when supplied. Keep their IDs and source dates. Company research is sufficient when individual research is absent.

Infer routine choices; ask only for context that materially changes the message. Default to one unsent initial email per group. Add named recipients, follow-ups or platform exports when requested. Supply your own approved pitches, content catalog and campaign board URL; this download includes no working campaign data.

## 2. Choose the problem and content together

Choose one buyer problem, one useful content offer and one compatible pitch. The opening is a direct work problem or a sourced customer story. Connect the same problem to the recipient's function and seniority. Do not assert an inferred pain as a known account problem.

Keep historical examples at their actual date. Do not invent customer emotions, outcomes, personal behavior, technology adoption or familiarity. Account-level intent is not an individual's behavior. Keep private CRM and intent details out of buyer copy.

## 3. Draft for each group

Write: value subject, problem/story opening, company-and-role bridge, exact approved pitch, then a useful content CTA. Aim near 70-110 body words when practical. A resource-led campaign offers a story, guide or personalized page on its supplied board rather than asking for a meeting. Other campaign goals use the participant's stated action.

Select pitch text from the supplied library without rewriting it. New pitch wording is a separate review proposal. Use approved qualitative capability context when numeric proof is unavailable. Avoid em dashes, generic corporate phrasing and unsupported promises. End with the supplied signature and honor the campaign's footer policy.

For company batches, vary the relevant angle, subject and opening across sales recipients. Check AgentMail and Smartlead drafts together, including supplied prior messages. Pitches may repeat; complete messages must differ within a company/campaign/touch. Do not fill a quota with cosmetic variants or irrelevant angles. Rich account-level Marketing Emails use separate variation rules.

## 4. Check personalization and links

Trace account and customer claims to sources. The named story must match the content offer. Keep unresolved identities and eligibility in review notes; do not invent names, addresses or research. Role-only templates can retain explicit placeholders.

Keep one CTA destination. In a board-led campaign, every click returns to the supplied board or a verified item on that board. Code owns recipient identity, URL encoding and tokens. Without a resolved URL, retain the destination as a review gap. Do not invent a token or substitute an external case-study link.

For a named-recipient draft, preserve supplied suppressions, affiliation gaps and communication constraints. Missing eligibility does not block role-copy preparation.

## 5. Review the drafts

Review the whole message: does the subject promise the value offered, and do opening, bridge, pitch and CTA address the same problem? Check claim support, fixed pitch text, role relevance and account-level duplication. Use the offline [batch checker](scripts/check_email_batch.py) for the JSON contract; it checks structure and exact duplicates, not factual truth or sending eligibility.

For an AgentMail or Smartlead handoff, read only that provider's section in [delivery-handoffs.md](references/delivery-handoffs.md). Return actual copy, sources, review gaps and the requested files. All messages remain drafts. Importing, creating mailbox drafts, activating campaigns and sending require their own authorization and available tools. Skill installation creates no connection or permission to send.
