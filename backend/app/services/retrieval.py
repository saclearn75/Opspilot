from backend.app.config import TOP_K
from backend.app.db.chroma import get_or_create_collection
from backend.app.db.sqlite import get_db_connection
from backend.app.schemas.ask import ChunkResult


def retrieve_chunks(question: str) -> list[ChunkResult]:
    collection = get_or_create_collection()
    results = collection.query(
        query_texts=[question],
        n_results=TOP_K,
        include=["documents", "metadatas", "distances"],
    )

    if not results["ids"] or not results["ids"][0]:
        return []

    conn = get_db_connection()
    cursor = conn.cursor()
    chunk_results: list[ChunkResult] = []

    for rank, chunk_id_str in enumerate(results["ids"][0], start=1):
        chunk_id = int(chunk_id_str)
        distance = results["distances"][0][rank - 1] if results["distances"] else 0.0
        score = 1.0 / (1.0 + distance)

        cursor.execute(
            """
            SELECT c.chunk_text, c.document_id, d.title, d.source_type
            FROM chunks c
            JOIN documents d ON d.id = c.document_id
            WHERE c.id = ?
            """,
            (chunk_id,),
        )
        row = cursor.fetchone()
        if not row:
            continue

        chunk_results.append(
            ChunkResult(
                chunk_id=chunk_id,
                document_id=row["document_id"],
                title=row["title"],
                source_type=row["source_type"],
                chunk_text=row["chunk_text"],
                score=round(score, 4),
                rank=rank,
            )
        )

    conn.close()
    return chunk_results
