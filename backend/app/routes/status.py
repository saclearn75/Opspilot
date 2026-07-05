from fastapi import APIRouter

from backend.app.schemas.status import StatusResponse
from backend.app.services.status import get_status

router = APIRouter()


@router.get("/status", response_model=StatusResponse)
def status() -> StatusResponse:
    return get_status()
