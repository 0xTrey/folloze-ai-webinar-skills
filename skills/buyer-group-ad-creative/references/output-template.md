# Ad creative template

Return `buyer-group-ads.md`, plus visual draft files if generated. A build brief is a valid fallback, but is not a rendered asset or a placement-ready export.

## Campaign context

- Seller/product, Company Brain version, campaign goal
- Account, segment, buyer-group IDs and persona reference
- Tool-map ID/version, image/design/specification route IDs, access and allowance state
- Channel/placement and current official spec source, or pending
- Approved destination/CTA, or proposed and unverified
- Review state and owner

## One concept per record

```markdown
## {Concept ID}: {short concept name}

- Buyer-group ID: {stable group ID}
- Angle: {one role problem and relevant value}
- Headline: {one primary headline}
- Body: {brief supporting copy}
- CTA: {one action}
- Destination: {approved URL, participant-provided unverified URL, or missing}
- Layout: {headline, graphic, body, CTA placement and reading order}
- Visual: {specific scene, diagram, or approved product asset}
- Approved assets: {source/rights reference, or missing}
- Image/build prompt: {subject, composition, palette from supplied brand rules, exclusions, reserved text areas}
- Alt text: {brief description}
- Proof: {claim IDs, original scope and qualifiers; source notes outside ad copy}
- Rationale and learning question: {why this group and what to test}
- Production spec state: {verified source/date or pending}
- Preview: {actual file and inspection result, or not generated}
- Approval: Draft, pending {authorized reviewer}
```

## Review record

| Concept/group | Persona fit | Voice | Claim/source scope | Assets | Spec and destination state | Visual inspection | Decision needed |
|---|---|---|---|---|---|---|---|
| {IDs} | {finding} | {finding} | {approved basis or held} | {rights or missing} | {verified/pending} | {checked or not generated} | {owner/action} |

Keep rendered copy separate from private rationale and sources. Record local generation, external upload, ad setup, and launch separately. Only local drafts are part of this workflow.
