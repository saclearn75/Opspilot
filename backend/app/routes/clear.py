from fastapi import APIRouter, HTTPException

from backend.app.schemas.clear import ClearResponse
from backend.app.services.clear import clear_data

router = APIRouter()


@router.post("/clear", response_model=ClearResponse)
def clear() -> ClearResponse:
    try:
        return clear_data()
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
