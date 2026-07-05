---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "Bulk invite uploads fail with seasonal staff list",
  "project": "Onboarding",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-03-12",
  "tags": [
    "onboarding",
    "bulk-invite",
    "temporary-staff"
  ],
  "customer": "BrightPath Home Services",
  "status": "open",
  "priority": "medium"
}
---

# Support Ticket: Bulk invite uploads fail with seasonal staff list

## Customer
BrightPath Home Services

## Problem
A user reported: bulk invite uploads fail with seasonal staff list. The issue affects the onboarding workflow and may connect to previous feedback around onboarding, bulk-invite.

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
