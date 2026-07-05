# OpsPilot (MemoryOS2)

Institutional memory RAG demo: ingest markdown artifacts into SQLite + ChromaDB (local embeddings), then ask questions with OpenAI for answers.

## Prerequisites

- Python 3.11+
- Node.js 18+
- OpenAI API key (for LLM answers only; embeddings run locally via ChromaDB)

## Setup

1. Copy environment file and add your key:

```bash
cp .env.example backend/.env
# Edit backend/.env and set OPENAI_KEY
```

2. Install backend dependencies (from project root):

```bash
pip install -r backend/requirements.txt
```

3. Install frontend dependencies:

```bash
cd frontend
npm install
```

## Run

**Terminal 1 — backend** (from project root):

```bash
uvicorn backend.app.main:app --reload --port 8000
```

**Terminal 2 — frontend**:

```bash
cd frontend
npm run dev
```

Open http://localhost:5173

## Usage

1. Click **Read Data** to ingest sample markdown from `data/` (only works when databases are empty). Embeddings are created locally by ChromaDB — no OpenAI call required.
2. Enter a demo question and press Enter or **Submit**. (Uses OpenAI for the written answer.)
3. Click a chunk card to view the full source document with the chunk highlighted.
4. Click **Clear Data** to wipe SQLite and Chroma.

## API

- `GET /api/health`
- `GET /api/status`
- `POST /api/ingest`
- `POST /api/clear`
- `POST /api/ask` — body: `{ "question": "..." }`
- `GET /api/documents/{id}?highlight_chunk_id=...`

OpenAPI docs: http://localhost:8000/docs

## Regenerate frontend types from OpenAPI

With the backend running:

```bash
cd frontend
npm run generate:api
```
