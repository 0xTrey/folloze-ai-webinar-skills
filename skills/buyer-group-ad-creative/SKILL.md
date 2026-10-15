---
name: buyer-group-ad-creative
description: "Create B2B ad copy and rendered creative for LinkedIn single-image ads and 6sense display banners from company context and buyer groups. Return channel-sized assets, board destinations and review files without launching ads."
---

# Buyer Group Ad Creative

Turn the buyer group's work into a useful content offer, ad copy and visual files. Use the same campaign context as the sales email skill. Adapt the argument and layout to each placement.

Read [context-and-evidence.md](references/context-and-evidence.md). Use [platform-formats.md](references/platform-formats.md) for LinkedIn and 6sense, then [output-template.md](references/output-template.md) for the handoff. Start from supplied files. Read [tool-map-use.md](references/tool-map-use.md) when a connected operation is needed.

## 1. Read the group and brand

Use the Company Brain's voice, positioning, approved capabilities and proof. Add account briefs, buyer groups, useful content, approved brand assets and the campaign destination. Preserve their IDs and source dates. Company research is sufficient when individual research is absent.

When the participant supplies an ad, inspect it and reuse it as the starting point. Preserve its approved message and visual direction. Propose only necessary copy corrections, CTA changes and placement adaptations. Create new concepts only when requested or when the supplied creative cannot serve the goal. Without supplied creative, default to one concept for marketing leaders and one for practitioners when those groups exist; follow a supplied count or buyer map instead. Ask only when missing context materially changes the output.

## 2. Connect the problem and offer

Choose one recognizable work problem and one useful story, guide or campaign example. Leaders may care about account relevance and useful sales context; practitioners may care about reusing approved content and getting campaigns live. Tie the choice to the actual persona rather than treating these examples as facts about an account.

Use supported capabilities when approved outcome proof is unavailable. Preserve customer-story scope and qualifiers. Do not invent metrics, testimonials, customer emotion, familiarity or adoption. Keep private research and intent signals outside the ad. An account audience is not a named-person audience.

## 3. Write for the placement

Write one outcome headline, minimal supporting copy and one content CTA. For LinkedIn, separate the introductory text and platform headline from the words inside the image. For 6sense static banners, the copy lives in the image; do not apply native-ad title limits to a banner.

Keep approved elevator pitches intact in the source library. Ads can use a supported short capability statement; do not silently rewrite the approved pitch itself. Prefer a useful resource or campaign-page offer over a meeting request for a resource-led campaign.

Use the supplied campaign board as the click destination. Record its resource ID and verify that the offer is available there. A content source URL belongs in review notes, not as a substitute landing page. Code adds approved attribution parameters while preserving existing query values. Paid ads use non-personal channel/creative attribution, never invented recipient tokens or contact parameters. See [platform-formats.md](references/platform-formats.md).

## 4. Render and inspect

Use the real approved logo, brand colors and typography. Start with one primary headline. Avoid an eyebrow-headline-dek stack, em dashes, leading-zero labels, fake dashboards and unsupported proof.

Create actual editable source and raster exports with an available authorized design tool. Typography and workflow diagrams can use SVG, HTML or canvas; use an available image tool for photographic or illustrated concepts. Keep exact text and logos under deterministic control where practical. Recompose each aspect ratio instead of shrinking one master. A paid operation still needs a verified cost and scoped allowance.

For supplied raster creative, use an available image editing tool for content changes. Check spelling, generated interface text, CTA consistency and logo fidelity before resizing or exporting. Preserve explicit participant approval of a claim for its stated use.

Inspect the exported files at their actual placement size. Check legibility, unclipped text, logo proportions, contrast, dimensions and bytes. Use the bundled [export checker](scripts/check_ad_exports.py) for PNG files and the JSON manifest. It checks files and structure, not claims, design quality, platform acceptance or sending permission. When rendering is unavailable, return a complete brief and mark assets unrendered.

For a webinar or demonstration, build a clear gallery of supplied and generated concepts. Keep original artwork intact and label the view as a preview. Production exports and ad setup are optional unless requested.

## 5. Review and hand off

Return the copy, actual visual files, editable sources, platform handoff, evidence notes and learning question. Keep the JSON manifest and each asset in the same portable folder. Use stable concept and buyer-group IDs. New creative remains Draft until reviewed, even when its source claims are approved.

Record local generation separately from external upload, ad-account setup, audience validation, budget approval and launch. This skill creates no ad connection, budget or permission to launch. For another placement, verify its current official specs rather than extending these defaults by assumption.
