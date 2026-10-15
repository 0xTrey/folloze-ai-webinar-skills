# Buyer-group email template

Return `buyer-group-emails.md`. Keep content grouped by stable IDs, so a campaign builder can select the right message without relying on a person's name.

```markdown
# {Campaign}: buyer-group email drafts

- Seller/product and Company Brain version: {context}
- Tool map and routes: {map ID/version, route IDs, coverage and manual alternatives}
- Account and segment scope: {IDs}
- Goal and requested action: {one action}
- Channel/state: email; local unsent Draft
- Review owner: {confirmed owner or suggested role}

## {Email ID}: {buyer-group name}

- Buyer-group ID: {BG ID}
- Account/segment IDs: {IDs or role-only scope}
- Role job and message angle: {persona basis}
- Subject option 1: {short subject}
- Subject option 2: {optional alternative}

### Body

{Concise email text. Use a neutral greeting placeholder if recipient identity is unresolved. One CTA.}

### Review notes

- Body word count: {actual count}
- Personalization: {source ID and exact scope, or role-level copy with no claimed account pain}
- Capability and proof: {source/claim IDs, qualifiers, and held items excluded}
- Product limits respected: {limit}
- Destination: {URL and read-only check result, or reply-based CTA}
- Recipient/current role: {not assessed for role copy, verified source/date, or pending}
- Communication eligibility: {not assessed, held, or participant-confirmed scope; separate from copy approval}
- Approval: Draft, pending {reviewer}
- Next action: {copy review or precise evidence request}
```

Add a short source register if the source IDs are not already attached. Record claim approval for the stated use separately from approval of the new email. A word-count check or mailbox draft is not delivery evidence.

## Optional machine-readable batch

For a requested company batch, also return `email-drafts.json`. `pitches` is the supplied library, not a model approval. `company_key` is a consistent domain or source account ID. All rows remain drafts.

```json
{
  "campaign_id": "campaign-review",
  "destination_url": "https://example.com/campaign",
  "footer_policy": "signature_only",
  "pitches": [{"id": "P1", "text": "Exact supplied pitch", "approval": "approved"}],
  "drafts": [{
    "id": "D1", "company_key": "example-company", "touch": 1,
    "recipient_ref": "source-contact-1", "function": "abm", "seniority": "manager",
    "subject": "Give each buyer relevant proof",
    "opening": "One asset rarely answers every question inside a target account.",
    "bridge": "Different buying roles may need different proof before moving forward.",
    "pitch_id": "P1", "pitch_text": "Exact supplied pitch",
    "cta": "Explore the campaign example.", "board_url": "https://example.com/campaign",
    "resource_id": "campaign-example", "source_ids": [], "review_state": "draft"
  }],
  "prior_messages": []
}
```

Run the bundled checker from the skill's actual directory:

```text
python3 <skill-directory>/scripts/check_email_batch.py <email-drafts.json>
```

It reads only the local JSON. It checks required sections, fixed pitch text, campaign destination, signature-only footer policy and normalized subject/opening/body duplicates against current and supplied prior messages. It cannot approve claims, find unsupplied historical sends, reserve variants, validate recipient eligibility or contact an email platform. Review near duplicates and factual claims separately.

Add the selected provider handoff only when requested. Keep actual recipient addresses and identity URLs in protected files. Do not use the example domain, draft IDs or placeholder recipient references as real transport values.
