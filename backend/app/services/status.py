from backend.app.db.sqlite import get_db_connection, is_db_empty
from backend.app.schemas.status import StatusResponse


def get_status() -> StatusResponse:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM documents")
    document_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM chunks")
    chunk_count = cursor.fetchone()[0]
    conn.close()

    return StatusResponse(
        db_empty=is_db_empty(),
        document_count=document_count,
        chunk_count=chunk_count,
    )
