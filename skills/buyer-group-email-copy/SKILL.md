---
name: buyer-group-email-copy
description: "Draft B2B sales emails and LinkedIn messages using verified triggers, role relevance, fixed approved pitches and content CTAs. Prepare AgentMail or Smartlead handoffs without sending or enrolling contacts."
---

# Buyer Group Email Copy

Turn company context and buyer roles into reviewable sales emails and LinkedIn messages. The email framework works with AgentMail, Smartlead or another sender. This skill runs in the AI workspace; it does not install inside an email platform.

Read [context-and-evidence.md](references/context-and-evidence.md). Use [messaging-framework.md](references/messaging-framework.md) for trigger selection, email and LinkedIn formats, follow-ups and reusable prompts, then [output-template.md](references/output-template.md) for the handoff.

Start with supplied files. When connected research or storage is needed, read [tool-map-use.md](references/tool-map-use.md) and the participant's map. Drafting needs no contact enrichment or sending operation.

## 1. Read the message context

Use the Company Brain's voice, personas, product limits, approved pitches and proof. Add the account brief, buyer map, content catalog and campaign destination when supplied. Keep their IDs and source dates. Company research is sufficient when individual research is absent.

Infer routine choices; ask only for context that materially changes the message. Default to one unsent initial email per group. Add named recipients, follow-ups or platform exports when requested. Supply your own approved pitches, content catalog and campaign board URL; this download includes no working campaign data.

## 2. Choose the problem and content together

Choose one verified trigger or relevant work problem, one useful content offer and one compatible pitch. For personal posts, promotions, new roles and certificates, use a dated source no more than four calendar months old at drafting. Connect the hook to the buyer's work; omit unrelated praise. Without a suitable personal trigger, use sourced company context, a direct work problem or a supported customer story. Company research is sufficient. Keep the first sentence under 15 words and do not assert an inferred pain as a known account problem.

Keep historical examples at their actual date. Do not invent customer emotions, outcomes, personal behavior, technology adoption or familiarity. Account-level intent is not an individual's behavior. Keep private CRM and intent details out of buyer copy.

## 3. Draft for each group

For email, write: value subject, relevant opening, company-and-role bridge, exact approved pitch, then a useful content CTA on its own line. Aim for 70-110 body words and 2-6 subject words. Trim the surrounding copy before changing a fixed pitch. A resource-led campaign offers a story, guide or personalized page on its supplied board rather than asking for a meeting. Other campaign goals use the participant's stated action.

For requested LinkedIn copy, distinguish a connection note from an accepted-connection message and a follow-up. Use the channel formats in the framework; keep a supplied approved pitch exact in substantive messages. Carry the same account, buyer-group and source IDs across channels.

Select pitch text from the supplied library without rewriting it. New pitch wording is a separate review proposal. Use approved qualitative capability context when numeric proof is unavailable. Avoid em dashes, generic corporate phrasing and unsupported promises. End with the supplied signature and honor the campaign's footer policy.

For company batches, vary the relevant angle, subject and opening across sales recipients. Check AgentMail and Smartlead drafts together, including supplied prior messages. Pitches may repeat; complete messages must differ within a company/campaign/touch. Do not fill a quota with cosmetic variants or irrelevant angles. Rich account-level Marketing Emails use separate variation rules.

A requested follow-up adds relevant proof or another useful resource, with a shorter 45-80 word target. Do not repeat the first hook or write a generic reminder. Select proof by relevance first; name recognition is a tiebreaker. Verify the relationship, permission and exact claim before naming a customer. A customer logo does not establish its use of a specific AI workflow or a performance result. Respect current customer and opportunity routing rules separately from copy.

## 4. Check personalization and links

Trace account and customer claims to sources. The named story must match the content offer. Keep unresolved identities and eligibility in review notes; do not invent names, addresses or research. Role-only templates can retain explicit placeholders.

Keep one CTA destination. In a board-led campaign, every click returns to the supplied board or a verified item on that board. Code owns recipient identity, URL encoding and tokens. Without a resolved URL, retain the destination as a review gap. Do not invent a token or substitute an external case-study link.

When a named story has a verified native board item, link the CTA directly to that item. Keep the story, copy claim and destination aligned. In machine-readable batches, list clean verified item URLs in `verified_board_item_urls` and place the actual CTA destination in `cta_url`; the checker still rejects other boards and unlisted items.

For named email recipients, preserve the complete identity-bearing item URL in both HTML and plain text. Decode and compare the identity and touch parameters against the source contact before handoff. Public previews use clean URLs and never expose real recipient identity. Parameterized URLs are not opaque Folloze Individual Links, and a local URL check does not prove attribution.

For a named-recipient draft, preserve supplied suppressions, affiliation gaps and communication constraints. Missing eligibility does not block role-copy preparation.

## 5. Review the drafts

Review the whole message: does the subject promise the value offered, and do opening, bridge, pitch and CTA address the same problem? Check trigger date and relevance, claim support, fixed pitch text, role relevance and account-level duplication. Use the offline [batch checker](scripts/check_email_batch.py) for the email JSON contract; it checks structure and exact duplicates, not trigger freshness, factual truth, channel lengths or sending eligibility. Review LinkedIn wording and cross-channel repetition separately.

For an AgentMail or Smartlead handoff, read only that provider's section in [delivery-handoffs.md](references/delivery-handoffs.md). Return actual copy, sources, review gaps and the requested files. All messages remain drafts. Importing, creating mailbox drafts, activating campaigns and sending require their own authorization and available tools. Skill installation creates no connection or permission to send.
