---
{
  "company": "OpsPilot AI",
  "source_type": "product_decision",
  "title": "Introduce branch-level permission groups",
  "project": "Permissions",
  "author": "Maya Patel, Head of Product",
  "date": "2026-06-04",
  "tags": [
    "permissions",
    "security",
    "reporting"
  ],
  "status": "accepted"
}
---

# Product Decision: Introduce branch-level permission groups

## Decision status
accepted

## Background
This decision was made after reviewing customer feedback, support tickets, and recent meeting notes. The team wanted to avoid building a generic knowledge base and instead focus on project memory that can answer practical operational questions.

## Decision
Introduce branch-level permission groups.

## Rationale
- The strongest evidence came from repeated customer pain, not one-off feature requests.
- The team wanted to reduce support burden and improve activation.
- Engineering preferred a narrow implementation that preserved architectural clarity.
- Product wanted every retrieved answer to cite the source documents that supported it.

## Alternatives considered
- Build a larger generalized workflow platform.
- Store all documents in one untyped folder and infer source type later.
- Put everything into the vector database and skip SQLite metadata.
- Delay the work until after a larger redesign.

## Consequences
- Every artifact should include source_type, project, date, author, and tags.
- SQLite remains the source of truth for metadata and document records.
- Chroma stores chunks and embeddings for semantic retrieval.
- The app can filter first by project/source_type/date, then retrieve semantically.
