import sqlite3
from backend.app.db.sqlite import get_db_connection, init_db
from backend.app.db.chroma import clear_chroma_collection
from backend.app.schemas.clear import ClearResponse

def clear_data() -> ClearResponse:
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM document_tags")
        cursor.execute("DELETE FROM chunks")
        cursor.execute("DELETE FROM documents")
        conn.commit()
        clear_chroma_collection()
        return ClearResponse(message="All data cleared successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        raise Exception(f"Failed to clear SQLite data: {e}")
    finally:
        conn.close()