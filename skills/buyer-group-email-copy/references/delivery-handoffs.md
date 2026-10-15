# Email platform handoffs

Choose the requested provider. Prepare files only unless the participant separately authorizes an available operation. No connection, credential or sending permission comes with this skill.

Keep a single canonical draft ID, company/campaign/touch, pitch version, resource ID and review state across platforms. The sender owns recipient identity, suppressions, schedule, mailbox capacity and unique attempt reservations. Do not enroll the same person in both platforms as a side effect of producing two exports.

## AgentMail

Return a protected `agentmail-messages.json` with one recipient per message, sender/inbox reference and subject, plain text and lightweight HTML. Use the actual resolved first name. Use one human CTA label in HTML and preserve the exact supplied identity-bearing URL in its href. Do not construct a Folloze-issued token with a language model.

The payload shape is `to: [resolved_email]`, `subject`, `text`, `html`, and `track_opens: false` unless an approved campaign explicitly requires tracking. Keep mapping-only review fields outside the provider payload. Without a recipient or resolved URL, return the draft and its gap rather than a send-ready payload.

Hand reviewed drafts to your approved AgentMail campaign workflow. Do not repurpose a live campaign's configuration or ledger. If no approved sender workflow is available, end with the files.

After separately authorized sending, actual message and thread IDs establish provider acceptance. Stored-message readback checks rendered names, exact copy and links. Delivery and human engagement require their own receipts.

Official field reference, checked October 14, 2026: [AgentMail send message](https://docs.agentmail.to/api-reference/inboxes/messages/send). Recheck the current API when implementing transport.

## Smartlead

Return `smartlead-leads.csv` and `smartlead-sequence-template.html` for a paused review campaign. The CSV maps standard recipient columns plus these example custom variables for touch 1:

- `flz_subject_t1`
- `flz_greeting_t1`
- `flz_opening_t1`
- `flz_bridge_t1`
- `flz_pitch_t1`
- `flz_cta_t1`
- `flz_board_url_t1`
- `flz_signature_t1`

These are custom fields defined by this handoff, not built-in Smartlead field names. Subject: `{{flz_subject_t1}}`. Put the body variables into simple paragraphs, and use `{{flz_board_url_t1}}` as the CTA href with `{{flz_cta_t1}}` as visible text. The greeting includes the resolved first name. Keep real newlines in text/CSV values, and use the destination's supported escaping for text and hrefs. Additional requested touches get distinct field suffixes and useful new angles.

Map the CSV headers to custom variables in the target campaign. Smartlead supports custom variables in both subject and body. Inspect actual lead previews before activation, especially HTML escaping, the signature, platform-added footer settings and the identity link. Do not assume an arbitrary full-HTML custom field is rendered as markup. If mapping or HTML substitution cannot be verified, return the exact unresolved gap.

Do not import, replace an existing sequence or activate a campaign merely to verify this handoff. Use the existing approved workflow when available, or provide manual instructions. Producing a CSV is not an imported, scheduled or delivered campaign.

Official references, checked October 14, 2026: [CSV column mapping](https://helpcenter.smartlead.ai/en/articles/409-how-to-map-csv-columns-in-smartlead-campaigns), [custom variables](https://helpcenter.smartlead.ai/en/articles/159-what-are-variables-and-how-to-use-them-effectively-to-personalize-emails-on-smartlead), [campaign preparation and preview](https://helpcenter.smartlead.ai/en/articles/34-creating-a-cold-email-campaign).

## Identity-bearing board links

Use a verified URL supplied by the protected link workflow. Preserve its values and attribution when adapting the draft. For a configured Folloze parameter-link workflow, code maps `em`, `fn`, `ln`, `co` and `ro`; platform-issued Individual Links are a different mechanism and must come from Folloze. Content selection and identity construction remain outside model-written copy. Keep recipient URLs out of public examples and aggregate reports.

Keep the campaign's plain-text identity policy explicit. A clean public fallback loses parameter identity in that MIME part; never silently substitute it when the campaign requires identity on every click. Check the actual stored message after an authorized send.
