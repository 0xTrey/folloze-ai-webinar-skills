# Company brain template

Use Markdown so the brain can move between approved tools. Keep each core file short; add detail only when it changes a marketing decision.

```text
company-brain/
  README.md
  branding-and-voice.md
  ideal-customer-profile.md
  messaging.md
  product-positioning.md
  buyer-personas.md
  source-manifest.md
  gap-plan.md
  proof-and-claims.md
  review-and-tests.md
```

## Shared core-file header

Use this header in each of the five core files. Values in braces are fields to fill, not approval defaults.

```markdown
# {Core area}

- Company and scope: {company, product or business unit}
- Owner: {confirmed owner, or suggested role with confirmation pending}
- Approval: {Approved, Draft or Unknown; scope and confirmation reference}
- Last reviewed: {date or pending}
- Next review: {agreed date or cadence, or proposed cadence pending}

## Sourced context

| Statement or rule | Source and section | Evidence | Approval | Limits or flags |
|---|---|---|---|---|
| {specific statement} | {source ID and locator} | Sourced | {state} | {scope, freshness, conflict} |

## Proposed guidance

| Draft guidance | Basis | Evidence | Approval | Decision needed |
|---|---|---|---|---|
| {proposal} | {source IDs or participant input} | Inference | Draft | {review question} |

## Missing context

- {field}: Missing. {gap ID, request, suggested owner}
```

Even if a file has approved sections, label draft or unknown statements individually. An owner may approve a proposed rule without changing its evidence label from `Inference` to `Sourced`.

## Five core areas

| File | Minimum useful content |
|---|---|
| `branding-and-voice.md` | Brand idea; voice; preferred and avoided language; approved example; logo and asset locations; visual rules and accessibility guidance when supplied |
| `ideal-customer-profile.md` | Best-fit company traits; problems and use cases; qualification questions; disqualifiers; timing and segmentation rules; unknown thresholds |
| `messaging.md` | Audience problem; value; message pillars; supporting proof; objections; next step; language to use or avoid |
| `product-positioning.md` | Product and category; customer job; capabilities; alternatives; supported differentiation; dependencies and limits; roadmap claims kept separate |
| `buyer-personas.md` | Role and buying involvement; job to do; pain; priorities; questions; objections; proof needs; useful message; uncertainties |

Messaging describes what to say. Positioning explains the product's place among alternatives. Keep these consistent without duplicating entire sections.

## README.md

Record company, domain, purpose, intended users, product scope, approved AI workspace, storage location, version, readiness, owner, and file map. Mark unanswered setup fields unknown.

Record tool-map ID/version, used route IDs, verified access and coverage, and any manual alternative. A map describes available operations; it does not approve company claims or private-document use. Return named blocks when a mapped save route is unavailable.

State which files and claims are approved for which uses. Unapproved guidance supports exploration only. Resolve conflicts through the source owner; never select a winner silently.

Explain updates: check the source, revise affected statements, retain the decision history, rerun affected tasks, and record review. Add a small glossary here only when terms need clarification.

## source-manifest.md

| ID | Title and exact location | Owner | Source date/version | Access date | Allowed use | Approval evidence | Freshness/flags | Used in |
|---|---|---|---|---|---|---|---|---|
| S1 | {URL or relative filename; section/page} | {confirmed or unknown} | {date or unknown} | {date} | {scope or unknown} | {approver, date, scope, confirmation location or unknown} | {current, stale, unreadable, partial, conflict} | {files/claim IDs} |

Use a document link for cloud sources, and a relative filename plus section for local uploads. Do not expose private URLs or confidential excerpts outside the agreed workspace. For a permission gap, record only the safe request, not restricted file contents.

## gap-plan.md

| ID | Area and missing decision | Document request | Search terms | Suggested owner | State | Next action |
|---|---|---|---|---|---|---|
| G1 | {gap and effect on task} | {exact material needed} | {terms} | {role; confirmation pending} | {missing, locating, draft, waiting review, resolved} | {participant action or scaffold} |

Keep only actionable gaps. Link drafted replacements to the appropriate core file and retain their review requirement.

## proof-and-claims.md

| ID | Claim | Source and scope | Evidence | Approval | Use state | Required qualifier/owner decision |
|---|---|---|---|---|---|---|
| P1 | {exact claim or proposed wording} | {source, population, conditions, period} | {Sourced, Inference or Missing} | {Approved, Draft or Unknown} | {usable, conditional, held or prohibited} | {limits and approval reference} |

Only mark `usable` or `conditional` after approval for the intended use. Hold unsupported metrics, guarantees, comparisons, conflicting claims, and customer names or logos with unknown usage rights. Preserve source-specific qualifiers; never generalize a single customer's result.

## review-and-tests.md

- Intended use and review date
- Participant feedback and corrections
- Approving authority, scope, confirmation, and unresolved owner decisions
- Conflict register: source versions, disputed claim, impact, owner, resolution or held state

| Task and exact prompt | Actual output | Sources used | Specificity/voice | Evidence and labels | Gaps/conflicts | Result and correction |
|---|---|---|---|---|---|---|
| {campaign, ICP or persona task} | {output or relative artifact link} | {IDs} | {findings} | {findings} | {findings} | {pass, incomplete or fail; repair} |

Record final readiness with reasons, top unresolved actions, owner, next review, and version. Keep file creation, destination save/readback, AI retrieval, publication, and delivery as separate observed or untested states.
