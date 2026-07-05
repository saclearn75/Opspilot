---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "SLA timer does not pause when ticket is waiting on customer",
  "project": "Customer Escalations",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-03-10",
  "tags": [
    "customer_escalations",
    "sla",
    "workflow"
  ],
  "customer": "Bayview Veterinary Partners",
  "status": "open",
  "priority": "medium"
}
---

# Support Ticket: SLA timer does not pause when ticket is waiting on customer

## Customer
Bayview Veterinary Partners

## Problem
A user reported: sla timer does not pause when ticket is waiting on customer. The issue affects the customer escalations workflow and may connect to previous feedback around customer_escalations, sla.

## Impact
- Priority: medium
- Current status: open
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
