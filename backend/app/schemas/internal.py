from pydantic import BaseModel
from typing import List, Optional

class ParsedDocumentMetadata(BaseModel):
    company: str
    source_type: str
    title: str
    project: str
    author: str
    date: str
    tags: List[str]
    customer: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None

class ParsedDocument(BaseModel):
    metadata: ParsedDocumentMetadata
    body: str
    file_path: str

class ChunkRecord(BaseModel):
    chunk_text: str
    char_start: int
    char_end: int