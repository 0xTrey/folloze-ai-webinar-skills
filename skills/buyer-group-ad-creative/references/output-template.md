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

## Platform files and export manifest

Return editable sources, PNG exports, `linkedin-ads.csv`, `6sense-display.csv`, and `ad-creatives.json` when both channels are requested. Use the columns in [platform-formats.md](platform-formats.md). Include only the requested platforms. These files are review handoffs, not proof of import or launch.

The manifest lives beside its files. Use relative image paths. Each format is one row with a unique creative ID. Example fields:

```json
{
  "destination_url": "https://example.com/campaign",
  "creatives": [{
    "id": "leader-relevance-linkedin-1200x628",
    "concept_id": "leader-relevance", "buyer_group_id": "marketing-leader",
    "platform": "linkedin", "width": 1200, "height": 628,
    "image_file": "leader-relevance-linkedin-1200x628.png",
    "source_file": "leader-relevance-linkedin-1200x628.svg",
    "introductory_text": "Explore an example of relevant content for different buying roles.",
    "headline": "Give buyers relevant content", "cta": "Learn More",
    "destination_url": "https://example.com/campaign?utm_source=linkedin&utm_medium=paid_social&utm_campaign=campaign-review&utm_content=leader-relevance-1200x628",
    "resource_id": "campaign-example", "source_ids": ["approved-capability-1"],
    "review_state": "draft"
  }]
}
```

Use your own approved context and actual exported files. For 6sense rows, set `platform` to `6sense`, use a checked banner size and `utm_medium=display`. Run:

```text
python3 <skill-directory>/scripts/check_ad_exports.py <ad-creatives.json>
```

The checker reads local files only. It validates PNG headers, dimensions, byte limits, required LinkedIn copy, board URL, known identity fields and attribution. It does not decode the PNG, approve claims or verify platform acceptance. Inspect the real image separately.
