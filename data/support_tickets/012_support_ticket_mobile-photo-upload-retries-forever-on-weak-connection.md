---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "Mobile photo upload retries forever on weak connection",
  "project": "Mobile",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-03-18",
  "tags": [
    "mobile",
    "photo-upload",
    "offline"
  ],
  "customer": "Luma Learning Centers",
  "status": "investigating",
  "priority": "medium"
}
---

# Support Ticket: Mobile photo upload retries forever on weak connection

## Customer
Luma Learning Centers

## Problem
A user reported: mobile photo upload retries forever on weak connection. The issue affects the mobile workflow and may connect to previous feedback around mobile, photo-upload.

## Impact
- Priority: medium
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
