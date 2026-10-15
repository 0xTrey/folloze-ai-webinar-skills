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
