---
{
  "company": "OpsPilot AI",
  "source_type": "retro",
  "title": "Support handoff process retro",
  "project": "Onboarding",
  "author": "Leo Chen, Engineering Lead",
  "date": "2026-07-15",
  "tags": [
    "onboarding",
    "support",
    "handoff"
  ],
  "status": "completed"
}
---

# Retro: Support handoff process retro

## Summary
The team reviewed what happened, what signals were missed, and what should be captured in institutional memory so similar problems are easier to answer in the future.

## What happened
A recurring issue connected to onboarding surfaced across multiple sources. Some evidence existed in customer interviews, some in support tickets, and some in meeting notes. The team did not initially connect the dots because the information was scattered.

## Root cause
- Source documents were not linked by consistent metadata.
- Similar issues used different wording across customer, support, and engineering conversations.
- The team relied on memory from individual people instead of a searchable project record.
- The app needed both structured filters and semantic search.

## What went well
- Support captured detailed customer impact.
- Product identified patterns across accounts.
- Engineering preserved logs and release notes.
- Customer Success provided useful context from conversations.

## What should change
- Ingest every operational artifact with explicit metadata.
- Store artifacts by source type for human readability.
- Also maintain a global index so the app can ingest all sources together.
- Make retrieved answers cite source documents and explain confidence.

## Follow-up actions
- Add tags: onboarding, support, handoff
- Link this retro to related support tickets and customer interviews.
- Add demo question: "What do we know about onboarding problems and what did we decide?"
