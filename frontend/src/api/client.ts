import type {
  AskRequest,
  AskResponse,
  ClearResponse,
  DocumentResponse,
  ErrorResponse,
  IngestResponse,
  StatusResponse,
} from "../types/api";

class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
    public detail?: string | null,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

async function parseError(response: Response): Promise<ApiError> {
  try {
    const data = (await response.json()) as ErrorResponse & { detail?: string };
    const message = data.error || data.detail || response.statusText;
    return new ApiError(message, response.status, data.detail);
  } catch {
    return new ApiError(response.statusText, response.status);
  }
}

async function request<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, init);
  if (!response.ok) {
    throw await parseError(response);
  }
  return (await response.json()) as T;
}

export async function getStatus(): Promise<StatusResponse> {
  return request<StatusResponse>("/api/status");
}

export async function ingestData(): Promise<IngestResponse> {
  return request<IngestResponse>("/api/ingest", { method: "POST" });
}

export async function clearData(): Promise<ClearResponse> {
  return request<ClearResponse>("/api/clear", { method: "POST" });
}

export async function askQuestion(body: AskRequest): Promise<AskResponse> {
  return request<AskResponse>("/api/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
}

export async function getDocument(
  documentId: number,
  highlightChunkId?: number,
): Promise<DocumentResponse> {
  const params = highlightChunkId
    ? `?highlight_chunk_id=${highlightChunkId}`
    : "";
  return request<DocumentResponse>(`/api/documents/${documentId}${params}`);
}

export { ApiError };
