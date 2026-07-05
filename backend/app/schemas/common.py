from pydantic import BaseModel
from typing import Literal, Optional

class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None

class HealthResponse(BaseModel):
    status: str