from pydantic import BaseModel, Field
from typing import List

class ChunkResult(BaseModel):
    chunk_id: int
    document_id: int
    title: str
    source_type: str
    chunk_text: str
    score: float
    rank: int

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1)

class AskResponse(BaseModel):
    answer: str
    chunks: List[ChunkResult]