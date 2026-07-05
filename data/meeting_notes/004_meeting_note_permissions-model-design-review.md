---
{
  "company": "OpsPilot AI",
  "source_type": "meeting_note",
  "title": "Permissions model design review",
  "project": "Permissions",
  "author": "Maya Patel, Head of Product",
  "date": "2026-04-24",
  "tags": [
    "permissions",
    "security",
    "reporting"
  ]
}
---

# Meeting Notes: Permissions model design review

## Attendees
- Maya Patel, Head of Product
- Leo Chen, Engineering Lead
- Amina Okafor, Customer Success Lead
- Sara Kim, Product Designer

## Discussion
The team reviewed recent customer interviews, support tickets, and sales feedback. The main tension was whether to ship a narrow fix quickly or invest in a more durable workflow improvement.

Key points:
- Customer Success reported that similar questions are appearing across multiple accounts.
- Engineering noted that several bugs stem from unclear source-of-truth rules.
- Product argued that the demo should show cross-source memory, not just search.
- Design recommended showing retrieved evidence with citations so users trust the answer.

## Decisions
- Treat permissions as a project memory area.
- Link related customer interviews and support tickets by tag, customer, and date.
- Store source type explicitly in metadata rather than relying only on filename.
- Keep the first version simple: markdown files with YAML or JSON front matter.

## Action items
- Product: define demo questions for permissions.
- Engineering: update ingestion parser to read metadata from the file header.
- Customer Success: identify two accounts with relevant feedback.
- Design: mock a source citation panel for retrieved results.
