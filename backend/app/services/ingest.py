import glob
import os
import sqlite3

from backend.app.config import CHUNK_OVERLAP, CHUNK_SIZE, DATA_DIR
from backend.app.db.chroma import get_or_create_collection
from backend.app.db.sqlite import get_db_connection, is_db_empty
from backend.app.schemas.ingest import IngestResponse
from backend.app.services.chunker import chunk_text
from backend.app.services.parser import parse_markdown_artifact


def ingest_data() -> IngestResponse:
    if not is_db_empty():
        return IngestResponse(
            status="skipped",
            message="Databases already contain data",
        )

    conn = get_db_connection()
    cursor = conn.cursor()
    chroma_collection = get_or_create_collection()

    documents_ingested = 0
    chunks_created = 0

    md_files = glob.glob(os.path.join(str(DATA_DIR), "**", "*.md"), recursive=True)
    md_files = [f for f in md_files if os.path.basename(f) != "README.md"]

    for file_path in md_files:
        parsed_doc = parse_markdown_artifact(file_path)
        if not parsed_doc:
            continue

        try:
            cursor.execute(
                """
                INSERT INTO documents (
                    title, source_type, project, author, date,
                    customer, status, priority, file_path, body
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    parsed_doc.metadata.title,
                    parsed_doc.metadata.source_type,
                    parsed_doc.metadata.project,
                    parsed_doc.metadata.author,
                    parsed_doc.metadata.date,
                    parsed_doc.metadata.customer,
                    parsed_doc.metadata.status,
                    parsed_doc.metadata.priority,
                    parsed_doc.file_path,
                    parsed_doc.body,
                ),
            )
            document_id = cursor.lastrowid

            for tag in parsed_doc.metadata.tags:
                cursor.execute(
                    "INSERT INTO document_tags (document_id, tag) VALUES (?, ?)",
                    (document_id, tag),
                )

            text_chunks = chunk_text(parsed_doc.body, CHUNK_SIZE, CHUNK_OVERLAP)
            chunk_ids: list[str] = []
            chunk_texts: list[str] = []
            chunk_metadatas: list[dict] = []

            for i, (chunk_text_content, char_start, char_end) in enumerate(text_chunks):
                cursor.execute(
                    """
                    INSERT INTO chunks (
                        document_id, chunk_index, chunk_text, char_start, char_end
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (document_id, i, chunk_text_content, char_start, char_end),
                )
                chunk_id = cursor.lastrowid
                chunk_ids.append(str(chunk_id))
                chunk_texts.append(chunk_text_content)
                chunk_metadatas.append(
                    {
                        "document_id": document_id,
                        "source_type": parsed_doc.metadata.source_type,
                        "project": parsed_doc.metadata.project,
                        "date": parsed_doc.metadata.date,
                        "tags": ",".join(parsed_doc.metadata.tags),
                        "customer": parsed_doc.metadata.customer or "",
                        "file_path": parsed_doc.file_path,
                        "chunk_index": i,
                        "title": parsed_doc.metadata.title,
                    }
                )
                chunks_created += 1

            if chunk_texts:
                chroma_collection.add(
                    documents=chunk_texts,
                    metadatas=chunk_metadatas,
                    ids=chunk_ids,
                )

            documents_ingested += 1
            conn.commit()

        except sqlite3.Error:
            conn.rollback()
            raise

    conn.close()
    return IngestResponse(
        status="success",
        message="Successfully read in data",
        documents_ingested=documents_ingested,
        chunks_created=chunks_created,
    )
