from backend.app.db.sqlite import get_db_connection
from backend.app.schemas.documents import ChunkRange, DocumentResponse


def get_document(document_id: int, highlight_chunk_id: int | None = None) -> DocumentResponse:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM documents WHERE id = ?", (document_id,))
    doc = cursor.fetchone()
    if not doc:
        conn.close()
        raise ValueError(f"Document {document_id} not found")

    cursor.execute(
        "SELECT tag FROM document_tags WHERE document_id = ? ORDER BY tag",
        (document_id,),
    )
    tags = [row["tag"] for row in cursor.fetchall()]

    cursor.execute(
        """
        SELECT id, chunk_index, char_start, char_end
        FROM chunks
        WHERE document_id = ?
        ORDER BY chunk_index
        """,
        (document_id,),
    )
    chunk_ranges = [
        ChunkRange(
            chunk_id=row["id"],
            chunk_index=row["chunk_index"],
            char_start=row["char_start"],
            char_end=row["char_end"],
        )
        for row in cursor.fetchall()
    ]

    conn.close()

    return DocumentResponse(
        id=doc["id"],
        title=doc["title"],
        source_type=doc["source_type"],
        project=doc["project"],
        author=doc["author"],
        date=doc["date"],
        customer=doc["customer"],
        status=doc["status"],
        priority=doc["priority"],
        file_path=doc["file_path"],
        body=doc["body"],
        created_at=doc["created_at"],
        tags=tags,
        chunks=chunk_ranges,
        highlight_chunk_id=highlight_chunk_id,
    )
