from fastapi import APIRouter, HTTPException, Query

from backend.app.schemas.documents import DocumentResponse
from backend.app.services.documents import get_document

router = APIRouter()


@router.get("/documents/{document_id}", response_model=DocumentResponse)
def fetch_document(
    document_id: int,
    highlight_chunk_id: int | None = Query(default=None),
) -> DocumentResponse:
    try:
        return get_document(document_id, highlight_chunk_id=highlight_chunk_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
