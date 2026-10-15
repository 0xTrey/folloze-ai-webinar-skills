# Build your first campaign

Use these ten skills to turn your company context and account list into campaign research, buyer groups, and draft creative. Start with one small campaign and your own inputs.

## Bring these inputs

- Your company URL and one campaign goal.
- A small account list with company names and domains. Start with accounts you can review individually.
- Approved brand, product, ICP, messaging, or customer-proof documents, when available. Missing documents are a starting point, not a reason to invent claims.
- An AI workspace approved for your company data. Use the tools and exports you already have.

You can start the planning work without a Folloze account. Building or publishing a Folloze page and reading its engagement data require the appropriate Folloze access and permissions.

## 1. Get the skills

[Download the full skills pack](https://github.com/0xTrey/folloze-ai-webinar-skills/raw/refs/heads/main/downloads/folloze-ai-webinar-skills.zip) and unzip it. Each folder under `skills/` contains one skill, its instructions, and the files it needs.

For Claude, [download the Claude campaign kit](https://github.com/0xTrey/folloze-ai-webinar-skills/raw/refs/heads/main/downloads/claude-campaign-kit.zip) and unzip it. Upload each individual ZIP in `skill-zips/` as its own skill.

Claude skills require **Code execution and file creation**. On individual plans, check **Settings > Capabilities**. On Team or Enterprise, an owner may need to enable code execution and Skills under **Organization settings > Plugins & skills > Policy**. Then open **Customize > Skills > + > Create skill > Upload a skill**, upload an individual skill ZIP, and enable it. See [Claude's current skill setup instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
If your AI tool does not support skill installation, attach the chosen skill's `SKILL.md` and referenced files together. Ask it to read those instructions before starting. Installing a skill supplies instructions, not access to your CRM, files, or marketing tools.

## 2. Start with your company

Open a new chat. Attach approved company documents you want the AI to use, then send:

```text
Help me build a campaign for {company URL}. Our goal is {campaign goal}. Use Company Brain Builder from this pack and the approved documents I attach. Start with the brand, ICP, positioning, messaging, and buyer personas. Cite sources, separate facts from assumptions, and show gaps before drafting replacements.

Then use Tools & Data Setup to map the tools and exports available in this workspace. If a connection is missing, tell me the smallest file I can upload instead. Give me named files I can save in my approved private workspace.

Work one step at a time. Ask only for information that changes the result. Keep new work in draft and stop for my review before sending, spending, publishing, or launching anything.
```

Review the Company Brain before applying it to your accounts. Correct unsupported claims and keep unresolved decisions visible.

## 3. Build in campaign order

Use the [20 campaign prompts](https://github.com/0xTrey/folloze-ai-webinar-skills/blob/main/CAMPAIGN-PROMPTS.md) one at a time. Each prompt names the inputs, matching skill, and output to review.

| Work | What to bring | What to review |
|---|---|---|
| Company Brain and tools | Company URL, approved documents, tool names | Source-backed context, gaps, and a tool map |
| Account list and segmentation | Your account CSV and campaign rules | Account identities, exclusions, explainable groups, and the first wave |
| Account briefs | Selected accounts, Company Brain, available research | Account facts, dated changes, a why-now hypothesis, and sources |
| Buyer groups | Reviewed briefs and known contacts, when available | Role needs, useful content, and contact-coverage gaps |
| Ad creative and email | Approved brand assets, pitches, content, and destination | Distinct messages for each buyer group and draft channel files |
| Buyer experience and follow-up | Reviewed campaign work and real engagement data | A page draft or prototype, reviewed links, and useful next actions |

The ten included skills cover the campaign map, tool setup, Company Brain, account-list building, segmentation, account briefs, buyer groups, ad creative, email copy, and engagement follow-up. Other prompt cards describe general workflows; they are not additional installed skills or automatic integrations.

## 4. Keep your work connected

Carry the latest Company Brain, `tool-map.md`, and relevant outputs into each new chat. Keep the same account, segment, and buyer-group IDs. A new chat does not automatically inherit earlier files.

Campaign Workspace is an optional map for the work. Open its packaged HTML app in a browser, create a campaign with your own name, and upload your sources. If you use the app beside your AI chat, upload files to each separately. Upload reviewed outputs to their matching stages and record your review after inspecting them.

The app stores campaign progress in your browser. Export the campaign record and save the original source and output files in your approved private workspace. The campaign JSON is not a backup of those files. Direct folder access or automatic updates require a separately configured compatible connector.

## 5. Review before activation

Check the account set, facts, proof permissions, buyer relevance, destinations, and new creative. Keep unknowns visible. Planning readiness does not establish that a page is published, an email was delivered, or a campaign produced results.

The public downloads do not connect your tools, configure Marketo, send sales emails, launch ads, or buy enrichment credits. Those actions require the right access, configuration, and your approval. Keep company documents, contacts, credentials, and campaign outputs out of the public repository.
