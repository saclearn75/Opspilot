---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "CSV import rejects valid branch names with trailing spaces",
  "project": "Integrations",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-02-28",
  "tags": [
    "integrations",
    "csv-import",
    "onboarding"
  ],
  "customer": "Riverline Logistics",
  "status": "resolved",
  "priority": "high"
}
---

# Support Ticket: CSV import rejects valid branch names with trailing spaces

## Customer
Riverline Logistics

## Problem
A user reported: csv import rejects valid branch names with trailing spaces. The issue affects the integrations workflow and may connect to previous feedback around integrations, csv-import.

## Impact
- Priority: high
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
