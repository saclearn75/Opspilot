---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "Calendar sync duplicates appointments after staff location change",
  "project": "Scheduling",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-03-02",
  "tags": [
    "calendar-sync",
    "scheduling",
    "integrations"
  ],
  "customer": "Evergreen Senior Care",
  "status": "investigating",
  "priority": "high"
}
---

# Support Ticket: Calendar sync duplicates appointments after staff location change

## Customer
Evergreen Senior Care

## Problem
A user reported: calendar sync duplicates appointments after staff location change. The issue affects the scheduling workflow and may connect to previous feedback around calendar-sync, scheduling.

## Impact
- Priority: high
- Current status: investigating
- Affected users: operations managers and customer success teams
- Business risk: additional support load, delayed adoption, or missed escalation ownership

## Timeline
- Customer reported the problem through support.
- Support reproduced the issue in the staging environment when possible.
- Engineering reviewed logs and related recent releases.
- Product tagged this issue for MemoryOS-style retrieval because similar symptoms appear across multiple accounts.

## Current hypothesis
The issue is likely caused by a mismatch between stored source-of-truth state and derived workflow state. The system needs clearer validation before data is embedded, synced, or surfaced in reports.

## Next steps
- Add this ticket to the relevant project memory.
- Link to customer interviews with overlapping tags.
- Confirm whether the fix should be a product improvement, a data migration, or a support playbook update.
