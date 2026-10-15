# LinkedIn and 6sense handoffs

Checked October 14, 2026. Recheck official specifications before a new production handoff. These defaults cover static creative only.

## LinkedIn single-image ads

- PNG or JPG, at most 5 MB. Default landscape export: 1200 x 628 pixels. Optional square: 1200 x 1200.
- Keep introductory text within the recommended 150 characters and platform headline within 70. These are recommendations, not a claim about hard input limits.
- Use a supported platform CTA such as Learn More. Inside the image, a more specific label may identify the content offer.
- Return `linkedin-ads.csv`: `creative_id`, `buyer_group_id`, `ad_name`, `introductory_text`, `headline`, `cta`, `destination_url`, `image_file`, `alt_text`, `review_state`.
- The CSV is a handoff sheet, not a promised bulk-import schema. Inspect the actual Campaign Manager preview before a separately authorized launch.

Source: [LinkedIn single-image specifications](https://business.linkedin.com/advertise/ads/sponsored-content/single-image-ads-specs).

## 6sense static display banners

- JPEG, JPG or PNG. Accepted sizes: 160 x 600, 300 x 250, 300 x 600, 320 x 480, 320 x 50 and 728 x 90 pixels.
- Official accepted file size: 1 KB minimum, 150 KB maximum. Use a conservative 150,000-byte ceiling and 1,024-byte floor in the checker.
- Default first set: 300 x 250, 300 x 600 and 728 x 90. Use a placement-specific headline, logo and readable CTA. Leave out supporting copy when the small format needs space.
- Return `6sense-display.csv`: `creative_id`, `buyer_group_id`, `ad_name`, `width`, `height`, `image_file`, `click_url`, `review_state`.
- These are handoff columns, not an automatic import contract. A static image does not include a click URL; the operator sets that URL on the ad record. Native and HTML5 formats have different requirements.

Sources: [6sense ad types](https://support.6sense.com/docs/6sense-campaign-ad-types-and-sizes), [official static-banner specification image](https://cdn.us.document360.io/0e2cd0a2-b3b3-495b-80df-96f8381febea/Images/Documentation/image-1773314176191.png).

## Board links and identity

Keep the supplied board host/path and any approved query parameters. Use code to add `utm_source` (`linkedin` or `6sense`), `utm_medium` (`paid_social` or `display`), an agreed `utm_campaign`, and a stable creative/format `utm_content`. Encode values with a URL library.

An anonymous ad click does not establish a named person's identity. Never add `em`, `fn`, `ln`, `co`, `ro`, a recipient token, or a contact ID to a general paid-ad URL. If a supplied URL already contains those fields, request a public ad destination. Valid existing first-party recognition can operate independently; do not claim it was verified by the ad export.

If an approved campaign requires a deep link, use its verified board-item URL. Do not guess a hash anchor or use the external source article instead. Platform click identifiers and macros require verification in the actual destination tool.

## Measurement

Choose one learning question per concept. Compare board visits and useful content engagement by creative, then account or buyer signals where actually available. Keep platform impressions, clicks, human board engagement and sales outcomes separate. Do not invent predicted CTR, conversions or attribution.
