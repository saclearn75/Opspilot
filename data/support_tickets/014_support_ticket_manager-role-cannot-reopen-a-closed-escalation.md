---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "Manager role cannot reopen a closed escalation",
  "project": "Permissions",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-03-22",
  "tags": [
    "permissions",
    "customer_escalations",
    "workflow"
  ],
  "customer": "Metro Appliance Repair",
  "status": "closed",
  "priority": "low"
}
---

# Support Ticket: Manager role cannot reopen a closed escalation

## Customer
Metro Appliance Repair

## Problem
A user reported: manager role cannot reopen a closed escalation. The issue affects the permissions workflow and may connect to previous feedback around permissions, customer_escalations.

## Impact
- Priority: low
- Current status: closed
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
