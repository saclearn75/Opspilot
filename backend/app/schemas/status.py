from pydantic import BaseModel

class StatusResponse(BaseModel):
    db_empty: bool
    document_count: int
    chunk_count: int