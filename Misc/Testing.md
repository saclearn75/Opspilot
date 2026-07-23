## 1. Sample data ingestion

- Click **Read Sample Data**.
- Verify the ingestion completes without errors.
- Verify the expected number of documents/chunks are created.
- Confirm embeddings are generated.
- Confirm ChromaDB is populated.

This is actually where you're failing right now, so we should fix this before anything else.

---

## 2. Database reset

- Click **Clear Database**.
- Confirm Chroma is emptied.
- Reload sample data.
- Verify duplicate documents are not created.

---

## 3. Retrieval pipeline

Ask several questions that require semantic retrieval rather than keyword matching.

Examples:

**Bug reports**

- What are the most common customer complaints?
- Which bugs affect login?
- Which issues are high priority?
- Which reports mention crashes?

**Customer interviews**

- What features are customers requesting?
- What pain points appear repeatedly?
- What are customers most frustrated by?
- Summarize the top product opportunities.

---

## 4. Grounding

For every answer verify:

- retrieved chunks are shown
- chunk ranking looks reasonable
- citations match the answer
- answer comes from retrieved context rather than hallucination

---

## 5. Document viewer

Click each retrieved chunk.

Verify:

- correct source document opens
- correct location is highlighted (if implemented)
- retrieved chunk matches the answer

---

## 6. Edge cases

Ask:

- a question that has no answer
- a vague question
- a misspelled question
- an unrelated question

Verify the system says it cannot find evidence instead of inventing an answer.

---

## 7. Performance

Measure:

- ingestion time
- embedding time
- retrieval time
- LLM response time

These become your deployment baseline.

---

## 8. Deployment readiness

Before moving to Lightsail, verify:

- backend starts cleanly
- frontend talks to backend
- no [localhost](http://localhost) references remain
- environment variables are loaded
- no CORS issues
- API endpoints all respond

---

### One thing I would add now

Since OpsPilot is going to become your **deployment template** for the other apps, I'd also test the backend independently of the frontend.

Open:

```

```

```
http://localhost:8000/docs
```

(or whatever port the backend uses)

Then exercise:

- `/status` 
- `/ingest` 
- `/query` 
- `/clear` 

If those all work in Swagger but the frontend doesn't, you immediately know the problem is in the Vite proxy or frontend. If they fail in Swagger too, it's a backend issue. That separation usually cuts debugging time dramatically.