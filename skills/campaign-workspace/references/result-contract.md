# Result contract

The connector returns a campaign ID and revision. Use the latest revision for writes; refresh after a conflict. Source records contain location, digest, check time, and verification state. Review is a separate user decision scoped to campaign planning.

For a skill result, link its output first, then return:

```json
{
  "id": "the-current-campaign-id",
  "revision": 3,
  "stepId": "segments",
  "result": {
    "summary": "Cohort assignments drafted for review.",
    "sourceIds": ["the-linked-output-source-id"],
    "blockingGaps": ["Account relationship holds still need review."]
  }
}
```

Step IDs: `brain`, `tools`, `accounts`, `segments`, `briefs`, `buyers`, `messages`, `experience`, `followup`. Do not create a source ID or digest in prose and call it verified. Tools results must use the capability-check operation. It currently covers local file handling and campaign storage only.

Pending skill slots do not prevent source linking or independent planning. Review gates remain tied to evidence and actual dependencies. An account import is not segmentation. A saved draft is not activation.
