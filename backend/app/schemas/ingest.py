from pydantic import BaseModel
from typing import Literal, Optional

class IngestResponse(BaseModel):
    status: Literal["success", "skipped"]
    message: Optional[str] = None
    documents_ingested: Optional[int] = None
    chunks_created: Optional[int] = None