# MemoryOS Synthetic Startup Dataset

This is a synthetic institutional-memory dataset for **OpsPilot AI**, a fictional startup.

## What is inside

There are 60 markdown artifacts across five human-readable folders:

- `customer_interviews/`
- `support_tickets/`
- `meeting_notes/`
- `product_decisions/`
- `retros_postmortems/`

Each file includes a JSON metadata block at the top, followed by the document body.

Example:

```markdown
---
{
  "company": "OpsPilot AI",
  "source_type": "support_ticket",
  "title": "CSV import rejects valid branch names with trailing spaces",
  "project": "Integrations",
  "author": "Nate Brooks, Support Lead",
  "date": "2026-02-28",
  "tags": ["integrations", "csv-import", "onboarding"],
  "customer": "BrightPath Home Services",
  "status": "resolved",
  "priority": "high"
}
---

# Support Ticket...
```

## Recommended app design

Keep the source files organized by directory for humans, but do not rely on folders alone.

Your app should read each `.md` file, parse the metadata header, and store:

### SQLite

Use SQLite as the source of truth.

Suggested tables:

- `documents`
  - `id`
  - `title`
  - `source_type`
  - `project`
  - `author`
  - `date`
  - `customer`
  - `status`
  - `priority`
  - `file_path`
  - `body`
  - `created_at`

- `document_tags`
  - `document_id`
  - `tag`

- `chunks`
  - `id`
  - `document_id`
  - `chunk_index`
  - `chunk_text`

### ChromaDB

Use Chroma for semantic search.

For each chunk, store:

- chunk text
- embedding
- metadata copied from SQLite:
  - `document_id`
  - `source_type`
  - `project`
  - `date`
  - `tags`
  - `customer`
  - `file_path`

## Why metadata belongs in the artifact

For this version, metadata should be written inside each artifact, not generated only by the app.

Reason:

- The document knows what it is.
- The app should not guess whether something is a meeting note or support ticket.
- Filenames and folders help humans, but metadata gives your ingestion pipeline reliable structure.
- Later, when ingesting Gmail, Slack, GitHub, or Notion, the connector can create equivalent metadata automatically.

## Demo questions to test retrieval

Try asking MemoryOS:

1. What do we know about onboarding problems?
2. Which customers complained about notification noise?
3. Why did we decide to keep SQLite separate from Chroma?
4. What incidents involved permissions or branch visibility?
5. What did we learn from CSV import failures?
6. What are the recurring mobile reliability issues?
7. Which product decisions were driven by customer interviews?
8. Summarize what we know about escalation ownership.
9. Show evidence that support load is tied to onboarding friction.
10. What should the team prioritize next based on repeated patterns?

## Ingestion recommendation

Start simple:

1. Recursively read all `.md` files under this dataset.
2. Parse the JSON metadata between the first pair of `---` markers.
3. Store metadata and body in SQLite.
4. Chunk the body.
5. Store chunks in SQLite.
6. Embed chunks into Chroma with metadata.
7. When querying:
   - optionally filter by `project`, `source_type`, `date`, or `customer`
   - perform vector search
   - return answer with cited file titles and source snippets
