from pydantic import BaseModel
from typing import List, Optional

class ChunkRange(BaseModel):
    chunk_id: int
    chunk_index: int
    char_start: int
    char_end: int

class DocumentResponse(BaseModel):
    id: int
    title: str
    source_type: str
    project: str
    author: str
    date: str
    tags: List[str]
    customer: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    file_path: str
    body: str
    created_at: str
    chunks: List[ChunkRange]
    highlight_chunk_id: Optional[int] = None