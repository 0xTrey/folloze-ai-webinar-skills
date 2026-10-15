# 20 prompts for your next campaign

Copy a prompt into your AI workspace. Replace the braces and attach the listed inputs. Each prompt can start a separate chat; carry the latest files into the next one.

Start with your own company, accounts and content. These prompts distill the build decisions from the Folloze webinar into reusable work. They include no working campaign data.

**Included skill** links point to the eight-skill pack. **Workflow prompt** means there is no dedicated operational skill for that action in this pack; the prompt works from your files and any tools actually available.

Ask for sources and inspect the result. New copy, creative and pages stay drafts. A tool connection does not authorize spending, sending, publishing or an ad launch. Choose your approved workspace for private inputs.

## Follow the campaign workflow

| Campaign section | Prompts | What you make |
|---|---|---|
| Setup | 1-2 | Company Brain and tool map |
| 1. Account list | 3 | Reconciled target list |
| 2. Segmentation | 4-5 | Explainable cohorts and a first-wave brief |
| 3. Account briefs | 6-7 | One reviewed pilot, then a focused batch |
| 4. Buyer groups | 8-9 | Role map and verified contact coverage |
| 5. Channel Activation | 10-16 | Channel plan, pitches, email, social and ad creative |
| 6. Buyer experience | 17-18 | Resource-first page draft and reviewed links |
| 7. Sales follow-up | 19-20 | Engagement report and useful sales follow-up |

Follow the [customer setup guide](https://github.com/0xTrey/folloze-ai-webinar-skills/blob/main/CUSTOMER-GUIDE.md) to install skills, or attach each skill's instructions and references together. [Download the skill pack](https://github.com/0xTrey/folloze-ai-webinar-skills/raw/refs/heads/main/downloads/folloze-ai-webinar-skills.zip). Use the optional Campaign Workspace app to track reviewed inputs and outputs.

## The prompts

### 1. Build the Company Brain

**Stage:** Setup
**Skill:** [Company Brain Builder](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/company-brain-builder)
**Bring:** Your company URL; any approved documents; a preferred storage location if known.
**Get:** A reusable Company Brain and a short document gap list.

```text
Use Company Brain Builder for {company URL}. Start with public research, then incorporate the approved documents I attach or authorize you to read. Organize branding and voice, ICP, messaging, product positioning and buyer personas.

Show what is sourced, inferred, missing or approved. For missing documents, tell me what to find and the role likely to own it; do not message anyone. Give me useful draft scaffolds so I can continue. Return the Company Brain files, proof-and-claims.md and a short gap list for {Google Drive, OneDrive or local folder}. If that storage is not connected, give me the files to save manually.
```

### 2. Map the tools and data we can actually use

**Stage:** Setup
**Skill:** [Tools & Data Setup](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/tools-data-setup)
**Bring:** Tool names; permitted folders or exports; any approved usage limits.
**Get:** tool-map.md with working routes and practical fallbacks.

```text
Use Tools & Data Setup. Our stack is {document storage, CRM, research or intent tools, email platforms, design tools and Folloze, where applicable}.

Check which connections are actually available with a small read-only test. Map where company context, account history, contacts, content and engagement data live. Separate access, operation permission and cost. Use only the usage limits I provide; otherwise start with zero charged operations. Return tool-map.md with verified routes, missing access and the exact export or upload that can substitute for each missing connection. Do not ask me to paste credentials into chat.
```

### 3. Turn the account list into something we can work with

**Stage:** 1. Account list
**Skill:** Workflow prompt
**Bring:** Account CSV or spreadsheet; Company Brain; available relationship records.
**Get:** accounts-reviewed.csv and account-review.md.

```text
Use this account list and our Company Brain to prepare the target universe for {campaign goal}. Preserve the original rows. Normalize company names and domains, flag likely duplicates, and retain parent and subsidiary distinctions.

Use supplied relationship records to distinguish customers, former customers, open opportunities and unknowns. Apply my campaign rules: {inclusions, exclusions and holds}. Do not infer current status from an old association. Return accounts-reviewed.csv with stable IDs, original row references and a disposition for every row. In account-review.md, reconcile raw rows and unique accounts and show the decisions I still need to make.
```

### 4. Segment the list around a shared buying problem

**Stage:** 2. Segmentation
**Skill:** [Campaign Segmentation](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/campaign-segmentation)
**Bring:** Reviewed account list; Company Brain; tool map.
**Get:** Cohort rules, account assignments and exceptions.

```text
Use Campaign Segmentation with our Company Brain, tool-map.md and reviewed account list. Propose a small set of cohorts based on a shared buying problem, use case or operating context. Explain when industry changes the message.

Give each cohort an entry rule, exclusion rule, campaign premise, relevant buyer roles and evidence gaps. Assign one primary cohort to each included account and explain the fit. Keep relationship holds visible. Return campaign-segments.md, account-segments.csv and a review queue. Reconcile every original account as included, held, review, excluded or duplicate. Do not force uncertain accounts into a campaign.
```

### 5. Choose the first campaign wave

**Stage:** 2. Segmentation
**Skill:** [Campaign Segmentation](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/campaign-segmentation)
**Bring:** Proposed segments; available content; campaign goal and constraints.
**Get:** first-wave-brief.md and the exact account set.

```text
Use Campaign Segmentation to help me choose the first wave from these proposed cohorts. Compare audience fit, available proof, content relevance, relationship context and our ability to execute. Recommend one cohort and explain the tradeoffs.

Build first-wave-brief.md with the campaign problem, buyer groups, useful content offer, account IDs, channel hypothesis and one learning question. Keep net-new, restart and customer motions distinct where our relationship rules require it. Show the exclusions and unresolved decisions. Treat your recommendation as a proposal for my review, then give me the exact account set to carry into research.
```

### 6. Build one account brief before we scale

**Stage:** 3. Account briefs
**Skill:** [Account Brief Builder](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/account-brief-builder)
**Bring:** One target company and domain; Company Brain; first-wave brief; tool map.
**Get:** One sourced pilot brief and a campaign hypothesis.

```text
Use Account Brief Builder for {target company and domain}. Use our Company Brain and first-wave brief to explain what this company does, who it sells to, why it fits and what may make the timing relevant.

Reuse available relationship history. Add primary company research and any accessible engagement, intent or technology evidence, keeping their sources and dates distinct. Missing access is not zero activity. End with one campaign hypothesis, useful content, buyer-role implications and open questions. Return one account brief with its source register. Build only this pilot so I can review its depth before we expand.
```

### 7. Apply the reviewed brief to the rest of the wave

**Stage:** 3. Account briefs
**Skill:** [Account Brief Builder](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/account-brief-builder)
**Bring:** Reviewed pilot; selected account IDs; Company Brain; tool map; review corrections.
**Get:** Individual briefs and an account comparison.

```text
Use Account Brief Builder to apply this reviewed pilot structure to {selected account IDs}. My corrections to the pilot are {decisions}. Keep the same account and segment IDs and reuse existing research before collecting more.

Write a distinct brief for each account. Preserve source dates, relationship context, observed signals and missing coverage. Tie each campaign hypothesis to that account's facts and our supported capabilities. Return the individual briefs plus account-briefs-summary.md comparing why each account belongs, what changes the message and what still needs review. Stay within the named accounts and the tool map's authorized usage limits.
```

### 8. Map the buying group and what each role needs

**Stage:** 4. Buyer groups
**Skill:** [Buyer Group Mapper](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-mapper)
**Bring:** Company Brain; account briefs; chosen campaign scope.
**Get:** Buyer groups with role jobs, questions and content needs.

```text
Use Buyer Group Mapper with these account briefs and our Company Brain. Map the roles involved in evaluating, approving, implementing and using our offering. Group people by the work they do and the evidence they need.

For each group, show the job, questions, objections, proof needs, useful content and message angle. Distinguish executive, manager and practitioner priorities. Preserve account and segment IDs and assign stable buyer-group IDs. Do not infer authority or reporting lines from a title. Return buyer-groups.md and a coverage table. A useful role-based map is enough where named contacts are unavailable.
```

### 9. Find the relevant people and show the coverage gaps

**Stage:** 4. Buyer groups
**Skill:** [Buyer Group Mapper](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-mapper)
**Bring:** Buyer map; account IDs; existing contacts or interaction exports; tool map.
**Get:** buyer-coverage.csv and a verification queue.

```text
Use Buyer Group Mapper to populate our buyer groups for {account IDs}. First reuse supplied CRM contacts, past interactions and research. Then use available, authorized sources to fill the relevant gaps.

Our desired coverage is {roles and approximate count per account}. Keep gaps when relevant people cannot be found. For every candidate, record current company and role evidence, source date, buyer-group fit, relationship history and what remains unverified. Keep historical employment separate from current affiliation. Return buyer-coverage.csv and a verification queue. Discovery, email verification and permission to contact are separate states. Use no charged lookup without an explicit allowance.
```

### 10. Turn the campaign into a channel plan

**Stage:** 5. Channel Activation
**Skill:** Workflow prompt
**Bring:** First-wave brief; buyer groups; content catalog; board URL; tool map.
**Get:** channel-activation-plan.md.

```text
Use our first-wave brief, buyer groups and content catalog to build a Channel Activation plan. The buyer-experience destination is {campaign board URL}.

For Marketing Emails, individual sales email, LinkedIn messaging, LinkedIn ads and 6sense ads, recommend the audience, role, useful offer, message approach and proposed next action. Explain which channels to start with and what makes the others worthwhile. Distinguish account-level HTML marketing email from individually addressed sales outreach. Keep every click on the campaign board or a verified content item there. Return channel-activation-plan.md with dependencies, a suggested owner role and the evidence we will use to judge each channel.
```

### 11. Build the pitch library we can approve once

**Stage:** 5. Channel Activation
**Skill:** [Buyer Group Email Copy](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-email-copy)
**Bring:** Company Brain; product capabilities; usable proof; existing approved pitches.
**Get:** pitch-library.md and a clear wording review.

```text
Use Buyer Group Email Copy with our Company Brain and product positioning. Reuse existing approved elevator pitches unchanged. If we do not have a library, propose five concise pitches covering distinct buyer problems and supported capabilities.

Show each pitch's exact text, intended use, source basis, version and approval state. Keep new wording in Draft for my review. Do not invent metrics or turn one customer's result into a general promise. Return pitch-library.md. Once I approve a version, use that exact pitch in later sales drafts; personalize the opening and role bridge around it. Propose future pitch changes separately.
```

### 12. Draft five sales emails, then prepare the batch

**Stage:** 5. Channel Activation
**Skill:** [Buyer Group Email Copy](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-email-copy)
**Bring:** Account briefs; buyer roster; approved pitches; content catalog; board URL.
**Get:** Five review drafts and the requested AgentMail or Smartlead handoff.

```text
Use Buyer Group Email Copy for {selected account and five representative buyers}. Write a value subject, problem or sourced customer-story opening, company-and-role bridge, exact approved pitch and content CTA to {campaign board URL}.

Company research is sufficient when individual research is absent. Make subjects, openings and complete messages meaningfully distinct within a company, including supplied prior Outreach, AgentMail and Smartlead messages. Pitches may repeat. Use resolved names and my supplied signature and footer policy. Return five drafts, evidence notes and email-drafts.json; run the bundled checker. After I review them, prepare the requested batch and {AgentMail JSON or Smartlead CSV/template} as unsent files. Keep unresolved recipient links flagged.
```

### 13. Build the account-level Marketing Email

**Stage:** 5. Channel Activation
**Skill:** Workflow prompt
**Bring:** Company Brain; account brief; approved brand assets; content offer; board URL.
**Get:** A rich HTML email draft, plain-text version and preview.

```text
Build a rich HTML Marketing Email for {account or cohort} using our Company Brain, approved assets and this offer: {content offer}. Link the CTA to {campaign board URL}. This is the account-level marketing message, so it can share copy across people at the same company.

Give me subject and preheader options, a clear content-led message, one primary CTA, lightweight email-compatible HTML and a plain-text version. Use the supplied sender, signature and footer policy. Keep merge fields explicit and separate them from resolved preview values. Return marketing-email.html, marketing-email.txt and a visual preview if available. Add Marketo mapping notes if relevant; do not claim an import or send.
```

### 14. Write the LinkedIn conversation

**Stage:** 5. Channel Activation
**Skill:** Workflow prompt
**Bring:** Buyer roles; account brief; optional individual research; content offer; board URL.
**Get:** A connection note and two useful message drafts.

```text
Use these buyer roles, account facts and approved content to draft LinkedIn outreach for {audience}. Write a short connection note, a first message offering something useful and one follow-up that adds a new reason to engage.

Adapt the opening for executive, manager and practitioner priorities. Use company context when personal research is unavailable, and do not invent familiarity or an observed pain. The connection note can omit a link; any content link must return to {campaign board URL} or a verified item there. Return the drafts with their evidence basis and unresolved personalization fields. Keep them as human-review messages, with no automated sending.
```

### 15. Create the LinkedIn ad creative

**Stage:** 5. Channel Activation
**Skill:** [Buyer Group Ad Creative](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-ad-creative)
**Bring:** Buyer groups; Company Brain; approved logo and assets; supplied ads if any; board URL.
**Get:** Copy, actual visual drafts and a review gallery.

```text
Use Buyer Group Ad Creative for LinkedIn with {priority buyer groups} and {campaign board URL}. Inspect any ads I supplied and reuse their approved message and visual direction. If we are starting fresh, propose two useful concepts based on the buyer's work and our content offer.

Return separate introductory text, platform headline and content CTA, plus actual visual drafts when a design tool is available. Check spelling, logo fidelity, supported claims and current LinkedIn specifications. Show a gallery so I can compare the concepts. Label webinar previews and production exports accurately. Include source notes and one learning question per concept. Do not upload or launch ads.
```

### 16. Adapt the concept for 6sense account advertising

**Stage:** 5. Channel Activation
**Skill:** [Buyer Group Ad Creative](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-ad-creative)
**Bring:** Reviewed creative; priority account group; content offer; board URL; intended use.
**Get:** 6sense visual variants or a webinar preview gallery.

```text
Use Buyer Group Ad Creative to adapt these reviewed concepts for 6sense account advertising. Preserve the approved message and brand. Recompose the layout for the requested display sizes rather than shrinking all the copy into one banner.

Our use is {webinar showcase or production preparation}. For a showcase, keep supplied artwork intact and make a clear gallery. For production preparation, verify current 6sense dimensions and file limits, export the requested sizes and run the bundled checker. Point every click to {campaign board URL} with non-personal channel and creative attribution. Return the assets and handoff notes. Audience targetability, budget and launch remain separate decisions.
```

### 17. Build a resource-first buyer experience

**Stage:** 6. Buyer experience
**Skill:** Workflow prompt; use your Folloze builder if available
**Bring:** Company Brain; campaign brief; buyer groups; approved content and assets; board URL if available.
**Get:** A saved Folloze draft or editable page prototype and content map.

```text
Build a resource-first buyer experience from our Company Brain, campaign brief, buyer groups and approved content. Lead with something useful to read, watch or explore. Create a strong opening, role-relevant content paths, approved customer proof and a clear next step.

Use the supplied visual references and real approved assets. Define an anonymous fallback and the account or persona variants we can support with evidence. If Folloze is connected, use its supported builder to save a draft at {board URL}. Otherwise return an editable HTML prototype and content map. Inspect the actual preview on desktop and mobile. Show what is built, what is proposed and what needs review before publication.
```

### 18. Connect each channel to the right board link

**Stage:** 6. Buyer experience
**Skill:** Workflow prompt; use the verified link workflow in your tool map
**Bring:** Board URL; contact or merge-field mapping; channel plan; approved link rules.
**Get:** channel-links.csv and a link QA report.

```text
Use our verified Folloze link workflow to connect these channel drafts to {campaign board URL}. Generate individually resolved links for named sales recipients, the documented merge-field pattern for Marketing Emails, and non-personal attribution links for public ads.

Keep one campaign ID and consistent channel and creative labels. Preserve existing query values and encode values with code. Distinguish documented identity-parameter links from Folloze-issued Individual Links; never invent a token. Keep personal URLs in protected files and use synthetic examples in the review. Return channel-links.csv and a decoded-value QA report. If the link workflow is unavailable, return the mapping and exact missing step rather than claiming identity pass-through works.
```

### 19. Read the engagement and show what happened

**Stage:** 7. Sales follow-up
**Skill:** Workflow prompt; works with a Folloze export
**Bring:** Board URL or ID; date range; engagement export or accessible analytics connection; channel map.
**Get:** engagement-summary.md and a reconciled engagement table.

```text
Analyze engagement for {Folloze board URL or ID} during {date range and timezone}. Use the connected analytics tools if available; otherwise work from the exports I attach. First show the sources, fields, filters and coverage actually available.

Summarize people and accounts that visited the board, content explored, repeat visits, engagement time and meaningful CTAs where those fields exist. Separate known buyers, anonymous account signals, suspected automation and unknown classification. Reconcile duplicates and explain the counting unit. Compare channels and creatives only where attribution supports it. Return engagement-summary.md and a table of useful signals, source records and limits. Keep email delivery, ad clicks and human board engagement distinct; do not infer buying intent from a visit.
```

### 20. Turn engagement into useful sales follow-up

**Stage:** 7. Sales follow-up
**Skill:** [Buyer Group Email Copy](https://github.com/0xTrey/folloze-ai-webinar-skills/tree/main/skills/buyer-group-email-copy) for email; workflow prompt for the full handoff
**Bring:** Engagement report; account brief; buyer context; content catalog; owner and relationship rules.
**Get:** sales-follow-up.md with context, drafts and next actions.

```text
Use this engagement report, account brief and buyer context to prepare sales follow-up. For a known buyer, explain the useful topic, what the evidence does and does not establish, the owner or proposed owner, and the next helpful action.

Use Buyer Group Email Copy for a concise email, plus draft a LinkedIn message and a phone opener where appropriate. Offer a relevant next resource on {campaign board URL}. Do not tell someone we observed behavior unless that wording is appropriate and supported. For anonymous account activity, propose an account-level action without assigning the visit to a person. Return sales-follow-up.md with source records, drafts, holds and a proposed follow-up test. Leave outreach unsent.
```

## Keep the work connected

Save each result with your own account, segment and buyer-group IDs. Reattach those files when opening another chat. If you use Campaign Workspace, link the outputs to the matching stage and record your review after inspecting them.

Bring your results back into your approved systems when you are ready. These prompts and skills do not install CRM, email, advertising or Folloze connections.
