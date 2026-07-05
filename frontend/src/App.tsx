import { useCallback, useEffect, useState } from "react";
import {
  ApiError,
  askQuestion,
  clearData,
  getDocument,
  getStatus,
  ingestData,
} from "./api/client";
import ChunkCardList from "./components/ChunkCardList";
import DocumentViewer from "./components/DocumentViewer";
import LlmOutput from "./components/LlmOutput";
import QuestionInput from "./components/QuestionInput";
import Sidebar from "./components/Sidebar";
import StatusBar from "./components/StatusBar";
import type { ChunkResult, DocumentResponse } from "./types/api";

export default function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [chunks, setChunks] = useState<ChunkResult[]>([]);
  const [selectedChunkId, setSelectedChunkId] = useState<number | null>(null);
  const [document, setDocument] = useState<DocumentResponse | null>(null);
  const [dbEmpty, setDbEmpty] = useState(true);
  const [loading, setLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState("Ready");
  const [statusError, setStatusError] = useState(false);

  const setStatus = useCallback((message: string, isError = false) => {
    setStatusMessage(message);
    setStatusError(isError);
  }, []);

  const refreshStatus = useCallback(async () => {
    try {
      const status = await getStatus();
      setDbEmpty(status.db_empty);
    } catch (err) {
      const message =
        err instanceof ApiError ? err.message : "Failed to fetch status";
      setStatus(message, true);
    }
  }, [setStatus]);

  useEffect(() => {
    void refreshStatus();
  }, [refreshStatus]);

  const handleReadData = async () => {
    setLoading(true);
    try {
      const result = await ingestData();
      if (result.status === "skipped") {
        setStatus(result.message || "Databases already contain data");
      } else {
        setStatus(
          result.message ||
            `Successfully read in ${result.documents_ingested} documents (${result.chunks_created} chunks)`,
        );
      }
      await refreshStatus();
    } catch (err) {
      const message =
        err instanceof ApiError ? err.message : "Failed to read in data";
      setStatus(message, true);
    } finally {
      setLoading(false);
    }
  };

  const handleClearData = async () => {
    setLoading(true);
    try {
      const result = await clearData();
      setAnswer("");
      setChunks([]);
      setSelectedChunkId(null);
      setDocument(null);
      setStatus(result.message);
      await refreshStatus();
    } catch (err) {
      const message =
        err instanceof ApiError ? err.message : "Failed to clear data";
      setStatus(message, true);
    } finally {
      setLoading(false);
    }
  };

  const handleAsk = async () => {
    const trimmed = question.trim();
    if (!trimmed) return;

    setLoading(true);
    setDocument(null);
    setSelectedChunkId(null);
    try {
      const result = await askQuestion({ question: trimmed });
      setAnswer(result.answer);
      setChunks(result.chunks);
      setStatus("Successfully received LLM information");
    } catch (err) {
      const message =
        err instanceof ApiError ? err.message : "Failed to get LLM response";
      setStatus(message, true);
    } finally {
      setLoading(false);
    }
  };

  const handleSelectChunk = async (chunk: ChunkResult) => {
    setSelectedChunkId(chunk.chunk_id);
    setLoading(true);
    try {
      const doc = await getDocument(chunk.document_id, chunk.chunk_id);
      setDocument(doc);
      setStatus(`Loaded document: ${doc.title}`);
    } catch (err) {
      const message =
        err instanceof ApiError ? err.message : "Failed to load document";
      setStatus(message, true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex min-h-screen flex-col bg-surface">
      <div className="flex flex-1 overflow-hidden">
        <Sidebar
          onReadData={handleReadData}
          onClearData={handleClearData}
          readDisabled={!dbEmpty}
          loading={loading}
        />
        <main className="flex flex-1 flex-col gap-5 overflow-y-auto p-6 pb-4">
          <h1 className="text-3xl font-bold tracking-tight text-accent-violet">
            OpsPilot
          </h1>

          <QuestionInput
            value={question}
            onChange={setQuestion}
            onSubmit={handleAsk}
            disabled={loading}
          />

          <div className="grid grid-cols-1 gap-4 lg:grid-cols-2">
            <LlmOutput answer={answer} />
            <ChunkCardList
              chunks={chunks}
              selectedChunkId={selectedChunkId}
              onSelectChunk={handleSelectChunk}
            />
          </div>

          <DocumentViewer document={document} />
        </main>
      </div>
      <StatusBar message={statusMessage} isError={statusError} />
    </div>
  );
}
