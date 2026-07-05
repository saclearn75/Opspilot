from fastapi import APIRouter, HTTPException

from backend.app.schemas.ingest import IngestResponse
from backend.app.services.ingest import ingest_data

router = APIRouter()


@router.post("/ingest", response_model=IngestResponse)
def ingest() -> IngestResponse:
    try:
        return ingest_data()
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
