# Rehearse a campaign in Claude

Use these 15 prompts for one walkthrough: an empty Folloze Campaign Workspace, connected context, an audience, and reviewable campaign drafts. The first prompt is the starter. Send the prompts one at a time.

## Set up once

1. [Download the Claude rehearsal kit](https://github.com/0xTrey/folloze-ai-webinar-skills/raw/refs/heads/main/downloads/claude-rehearsal-kit.zip) and unzip it. It contains the app, this guide, licenses, and eight individual skill ZIPs in `skill-zips/`.
2. In Claude, open **Settings > Capabilities** and enable **Code execution and file creation**. For Team or Enterprise, the owner may need to enable code execution and Skills in **Organization settings > Plugins & skills > Policy**. See [Claude's skills setup](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [artifact requirements](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them).
3. Open **Customize > Skills > + > + Create skill > Upload a skill**. Upload each ZIP in `skill-zips/` separately, then enable it. Do not upload the whole rehearsal kit as one skill. These menu labels were checked against Claude's documentation on October 14, 2026.
4. Confirm these eight skills are enabled: Campaign Workspace, Tools & Data Setup, Company Brain Builder, Campaign Segmentation, Account Brief Builder, Buyer Group Mapper, Buyer Group Ad Creative, and Buyer Group Email Copy. If your organization blocks uploads, ask its owner to provision these same ZIPs.
5. Prepare your own approved Company Brain files and a small account CSV in a private location. Use `Company` and `Domain` column headers; keep any other useful columns. Keep these files out of the public skills repository. For a short demo, use a list you can review on screen and research only three accounts. No company documents or contacts are included in this kit.

The app includes seven campaign skills; Campaign Workspace is the eighth skill installed in Claude. Installing a skill in Claude and attaching instructions inside the app are separate actions. Email copy and AgentMail or Smartlead handoff files are included. Marketo builds, live sales sending, cadence setup, Account List Builder, Buyer Experience Builder, and Follow-up & Measurement remain pending slots until their own skills are supplied.

## Start each rehearsal

1. Open a **new Claude chat** without company files or a preloaded company project. Attach `campaign-workspace.html` from the kit and send prompt 1.
2. Ask Claude to display the packaged app as an interactive artifact, preserving its code and Folloze design. Claude supports interactive artifacts, but this particular HTML file still needs a rehearsal in your Claude client. If it does not run there, open the same HTML file in a browser and keep Claude beside it.
3. In the app, click **New campaign**, enter a unique name such as `Webinar Rehearsal 1`, and click **Create campaign**. Do this even in a new chat: browser storage may retain previous campaigns. Confirm no campaign evidence is linked and no stages are ready. Missing and waiting states can have different colors.
4. Keep the app's **Campaign map**, **Knowledge tree**, and **Skills** views available. Add company files only at prompt 3 and the account CSV only at prompt 6.

### How chat and the app work together

**Public kit:** Claude reads the files you attach. The app reads files you upload into it. In browser mode, these are separate uploads. Use **Use skill** in the app to prepare a request, copy it into Claude, and download Claude's output for **Upload existing output** at the matching stage. Uploading an output replaces that stage's current output reference, so combine related files into one Markdown handoff while retaining their original sections and source IDs. Keep the originals in your private workspace.

**Existing compatible connector:** If Claude actually exposes Campaign Workspace tools such as `open_campaign` and `read_campaign`, use those tools with the current campaign ID and revision. Link allowed folders, record actual output sources, and read the campaign back after updates. The public kit does not install that connector. A typed folder path or an HTML attachment alone does not grant access or update the app.

In browser mode, **Tools & Data stays Not checked** because the app cannot run its connector capability check. A tool map in Claude does not turn this card green. With a connector, **Check workspace capabilities** verifies local workspace functions only, not CRM, Marketo, advertising, or sending access.

Review sources before clicking **Review for campaign planning > Record my review**. Green means ready for the next planning task. Drafts, pending skills, and missing dependencies remain visible. A green card does not establish activation or publication.

## The 15 prompts

Replace braces with your own values. Keep the starter's scope in effect throughout. After each output, use the app actions below or the verified connector equivalent.

### 1. Open an empty campaign

Attach `campaign-workspace.html` first.

```text
Use Campaign Workspace from the Folloze webinar pack. Read its instructions and runtime guidance. Open the attached packaged app as an interactive artifact, preserving its Folloze branding, layout, and readiness rules. Start a new, empty campaign named "Webinar Rehearsal 1". If the app needs a manual click, tell me the exact action.

Show the campaign map and confirm zero linked campaign inputs and zero ready stages. Keep the seven included campaign skills available. Do not reuse another campaign's company context or account list.

Work one stage at a time. Use only tools actually available here. If the Campaign Workspace connector is absent, return named files for manual upload and tell me the matching app action. Read live campaign state only through an exposed connector or the campaign JSON I attach; otherwise ask me to confirm it. Keep source evidence, draft guidance, and my review separate. Do not mark anything reviewed on my behalf. Do not send, publish, enroll contacts, or use charged services. After each step, state what changed, what is missing, and the next action.
```

**Show:** The empty map, seven included skills, pending slots, and the Knowledge tree with no campaign evidence. Eight skills installed in Claude does not mean eight completed campaign steps.

### 2. Map the tools we can use

```text
Use Tools & Data Setup. I use {document storage}, {CRM}, {contact or intent tools, if any}, and {creative tools}. Check what is actually exposed in this chat using read-only, uncharged operations. Return tool-map.md with tested access, unknowns, costs, and manual alternatives. Start the usage ledger with zero charged operations. Distinguish a named tool, a working connection, and permission to use an operation.
```

**Show:** Verified routes and manual alternatives. Keep the app's Tools & Data status unchanged unless its own connector capability check succeeds. Never request a password or API key in chat.

### 3. Bring in the prepared Company Brain

Attach your approved Company Brain files to Claude now. In browser mode, also select **Company Brain > Upload Company Brain files** and select the files together. Use Markdown or text files under 2 MB each.

```text
Use Company Brain Builder for {company name and domain}. Read the attached Company Brain and tool-map.md. If a verified connector can read my approved folder at {location}, reuse those files; otherwise use my attachments. Inventory branding and voice, ICP, messaging, positioning, and buyer personas. Link each area to the exact source and show its approval state. Reuse prepared material before drafting replacements.
```

**Show:** Five coverage areas, linked source files, and review still needed. Useful file names: `branding-and-voice.md`, `ideal-customer-profile.md`, `messaging.md`, `product-positioning.md`, and `buyer-personas.md`. The app uses names to identify coverage; Claude still needs to inspect the content.

### 4. Find the gaps

```text
Audit the Company Brain for this campaign. Return gap-plan.md and proof-and-claims.md. Separate missing documents, conflicting guidance, unsupported claims, and decisions I need to make. Reuse approved evidence. For anything missing, give me the smallest document request or a clearly labeled draft scaffold. Do not invent proof, customer permissions, or approval.
```

**Show:** One concrete gap and its next action. If there are none, show the evidence that supports that conclusion. Resolve blocking gaps before the next review. If you replace Brain files, upload the full current set together and review again.

### 5. Review and test the Company Brain

Send this only after reading the material and filling in your decisions.

```text
My Company Brain review decisions are: {approved areas and intended use; corrections; held claims}. Record these exact decisions in review-and-tests.md. Run three short retrieval tests: explain our ICP, adapt one message for a buyer role, and identify a claim we cannot use. Cite the source sections. Show whether this brain is ready for the agreed campaign-planning scope and what remains held.
```

**Show:** Inspect the retrieval tests, then record your planning review in the app if the result is acceptable and coverage is complete. A document containing five headings alone is not a useful Company Brain.

### 6. Add and reconcile the account list

Attach the account CSV to Claude. In the app, select **Account list > Upload account CSV** and upload the same file.

```text
Read this account CSV for {campaign goal}. Reconcile raw rows, unique accounts, duplicates, missing identities, and relationship exclusions. Preserve each original row and assign stable account IDs. Return account-list-review.md and a cleaned CSV only if needed. Show what changed and what needs my decision. Keep held or unresolved accounts out of active targeting.
```

**Show:** Raw and unique counts and one example of a duplicate, hold, or missing identity when present. Correct and reupload the CSV if needed. Review the final list in the app before segmentation is considered ready.

### 7. Create explainable segments

To demonstrate the app handoff, click **Use skill** beside Campaign Segmentation. Copy its prepared request into Claude, adding the scope below.

```text
Use Campaign Segmentation with the reviewed Company Brain, tool map, and reconciled accounts. Propose two or three useful segments based on evidence we actually have. Give each an entry rule, exclusion rule, buyer problem, campaign hypothesis, and draft CTA. Preserve account and row IDs. Return campaign-segments.md, account-segments.csv, and segmentation-review.md. Label assumptions and reconcile all dispositions.
```

**Show:** Why an account belongs in a group. Ask for one combined `segmentation-handoff.md` containing the three outputs for the app's single-file upload, then use **Segmentation > Upload existing output**. Preserve the original CSV separately.

### 8. Make the campaign choice

```text
My segmentation decisions are: {chosen segment, campaign goal, corrections, exclusions, and unresolved holds}. Apply these decisions, reconcile the counts again, and update the segmentation handoff. Show the exact account IDs we will use next and explain any remaining blocker. Record approval only for the scope I explicitly reviewed.
```

**Show:** Upload the revised combined handoff and record your review when acceptable. The Account list and Company Brain must also be reviewed for Segmentation to become ready.

### 9. Build three useful account briefs

```text
Use Account Brief Builder for three included accounts in our chosen segment. Use existing approved records first, then accessible primary sources where needed. Explain what each company does, what we know, observed engagement or Missing, relevant changes, and one campaign hypothesis. Cite sources and dates. Return the individual briefs plus one combined account-briefs.md for app upload. Keep inferred pain and unknown relationships explicit.
```

**Show:** One sourced fact beside one hypothesis. Upload `account-briefs.md` to **Account briefs** and review it before continuing. Research is scoped to these three accounts; do not silently expand it.

### 10. Map the buyer group

```text
Use Buyer Group Mapper for those same accounts and segment. Map role families, buying jobs, objections, proof needs, message angles, and content needs. Retain account, segment, and buyer-group IDs. Use supplied professional contacts only when relevant; otherwise keep this a role-based map. Do not infer decision authority from a title. Return buyer-groups.md and buyer-coverage.md, plus one combined buyer-group-handoff.md for the app. Use no paid enrichment.
```

**Show:** How two roles need different evidence or next steps. Upload `buyer-group-handoff.md` to **Buyer groups**, inspect it, and record the review if acceptable.

### 11. Draft buyer-group ad concepts

```text
Use Buyer Group Ad Creative with two priority buyer groups, our reviewed voice, approved brand assets, content catalog and board URL. Create one concept per group. Export LinkedIn 1200 x 628 images and 6sense 300 x 250, 300 x 600 and 728 x 90 banners. Include editable sources, platform copy, board tracking links, handoff sheets and ad-creatives.json. Run the included export checker and inspect the images. Return buyer-group-ads.md with source notes and one learning question per concept. If rendering is unavailable, mark the visuals unrendered. Keep every new creative in Draft; do not upload or launch ads.
```

**Show:** The difference between the buyer groups and between a brief and a rendered asset. Keep the ads in review until the messages handoff is complete.

### 12. Draft the emails and assemble the message handoff

```text
Use Buyer Group Email Copy for the same two groups. Draft one unsent email per group: value subject, problem or sourced customer story, company-and-role bridge, exact approved pitch, and one content CTA to our campaign board. Aim near 70-110 body words. Cite claims and role context in review notes. Keep subjects and openings distinct within each account. Return buyer-group-emails.md and combine it with buyer-group-ads.md into messages-and-creative.md for app upload. If requested, also prepare AgentMail or Smartlead handoff files. Keep Marketo builds, live sending, and cadence setup pending.
```

**Show:** Two different messages grounded in the same Company Brain. Upload the combined file to **Messages & creative**. Review the copy before recording the planning review. This does not configure a channel or establish outreach eligibility.

### 13. Design the buyer experience handoff

```text
Turn our reviewed segment, account briefs, buyer groups, and message drafts into buyer-experience-brief.md. Outline the page journey, role-specific content, approved proof, CTA, and source links. Show what can be reused and what still needs building. Check whether a matching builder skill is actually available. If it is pending, return a build-ready brief and preserve that pending status. Do not claim a page was built or published.
```

**Show:** Upload the brief to **Buyer experience** to show linked work. Keep the stage awaiting build or review when only a brief exists. Attaching a future skill does not itself complete the stage.

### 14. Plan the follow-up and measurement

```text
Draft followup-and-measurement.md for this campaign. Map meaningful buyer actions to a proposed next action, owner role, data source, metric definition, and test. Separate engagement signals from proof of buying intent. Identify the skills and connections needed for Marketo, sales outreach, and cadence execution. Keep owners unconfirmed unless supplied. Preserve dependencies on the buyer experience and mark unconfigured tracking or automation as pending. Do not activate anything.
```

**Show:** Upload the plan to **Follow-up & measurement**. A draft plan can be linked while its dependencies remain waiting. No measured result exists yet.

### 15. Show readiness and save the rehearsal

In browser mode, first click **Export campaign** and attach that JSON to Claude. It contains the actual stage and source-reference state. The HTML attachment alone does not let Claude inspect the running app.

```text
Use Campaign Workspace to review the campaign map and Knowledge tree. For each stage, report its actual state, linked sources, my review status, and the next blocker or action. Separate completed planning, draft work, pending skills, and untested connections. Return rehearsal-handoff.md with the campaign ID if available, decisions, file list, and next actions. Export the actual campaign record if the connector supports it; otherwise tell me to click Export campaign in the app. Do not invent a saved export or launch result.
```

**Show:** One linked source in the Knowledge tree, the honest stage states, and the downloaded campaign JSON. Save the JSON and source/output files privately. An imported campaign export needs its sources reattached and rechecked; it is not a complete source-file backup.

## Keep the live walkthrough moving

- Rehearse prompts 1 through 3 in the exact Claude client before the call. Native rendering and connector handoff are separate checks. No native Claude test is claimed by this guide.
- Have the approved Brain files and small CSV ready before screen sharing. Use prepared inputs during the call; use gap-building prompts when showing the path for someone starting without them.
- For a 30-minute example slot: setup and empty map, 3 minutes; tools and Brain, 7; accounts and segments, 6; briefs and buyers, 6; creative and email, 4; handoff and readiness, 4. Adjust for the webinar's actual slot. Generation and research time vary.
- If an input is missing, ask for the smallest useful upload or draft scaffold. Account List Builder is a pending slot, so do not present it as an included skill that ran.
- If an output is already prepared, upload that real file and describe it as prepared work. Do not simulate research or a connection delay.
- To rehearse again, export the current campaign, then choose **New campaign** with a new name. Keep the prepared source files and previous campaign intact.

The [public repository](https://github.com/0xTrey/folloze-ai-webinar-skills) contains reusable skills, the app, and this guide. Store your campaign inputs and outputs in your own approved private workspace.
