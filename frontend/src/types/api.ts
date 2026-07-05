/** API types aligned with backend Pydantic schemas */

export interface ChunkResult {
  chunk_id: number;
  document_id: number;
  title: string;
  source_type: string;
  chunk_text: string;
  score: number;
  rank: number;
}

export interface AskRequest {
  question: string;
}

export interface AskResponse {
  answer: string;
  chunks: ChunkResult[];
}

export interface IngestResponse {
  status: "success" | "skipped";
  message?: string | null;
  documents_ingested?: number | null;
  chunks_created?: number | null;
}

export interface ClearResponse {
  message: string;
}

export interface StatusResponse {
  db_empty: boolean;
  document_count: number;
  chunk_count: number;
}

export interface ChunkRange {
  chunk_id: number;
  chunk_index: number;
  char_start: number;
  char_end: number;
}

export interface DocumentResponse {
  id: number;
  title: string;
  source_type: string;
  project: string;
  author: string;
  date: string;
  tags: string[];
  customer?: string | null;
  status?: string | null;
  priority?: string | null;
  file_path: string;
  body: string;
  created_at: string;
  chunks: ChunkRange[];
  highlight_chunk_id?: number | null;
}

export interface ErrorResponse {
  error: string;
  detail?: string | null;
}
