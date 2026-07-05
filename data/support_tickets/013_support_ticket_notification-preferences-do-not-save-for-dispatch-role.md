---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "Notification preferences do not save for dispatch role",
  "project": "Notifications",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-03-20",
  "tags": [
    "notifications",
    "permissions",
    "dispatch"
  ],
  "customer": "Harbor MedSpa",
  "status": "resolved",
  "priority": "medium"
}
---

# Support Ticket: Notification preferences do not save for dispatch role

## Customer
Harbor MedSpa

## Problem
A user reported: notification preferences do not save for dispatch role. The issue affects the notifications workflow and may connect to previous feedback around notifications, permissions.

## Impact
- Priority: medium
- Current status: resolved
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
