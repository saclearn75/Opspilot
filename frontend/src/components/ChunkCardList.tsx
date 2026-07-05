import type { ChunkResult } from "../types/api";

interface ChunkCardListProps {
  chunks: ChunkResult[];
  selectedChunkId: number | null;
  onSelectChunk: (chunk: ChunkResult) => void;
}

export default function ChunkCardList({
  chunks,
  selectedChunkId,
  onSelectChunk,
}: ChunkCardListProps) {
  return (
    <div className="flex h-64 flex-col gap-2 overflow-y-auto rounded-lg border border-surface-border bg-surface-raised p-3">
      {chunks.length === 0 ? (
        <p className="text-sm text-slate-500">Retrieved chunks will appear here...</p>
      ) : (
        chunks.map((chunk) => (
          <button
            key={chunk.chunk_id}
            type="button"
            onClick={() => onSelectChunk(chunk)}
            className={`rounded-lg border p-3 text-left transition ${
              selectedChunkId === chunk.chunk_id
                ? "border-violet-400/60 bg-violet-500/10"
                : "border-surface-border bg-slate-800/40 hover:border-violet-400/30"
            }`}
          >
            <div className="mb-1 flex items-center justify-between gap-2">
              <span className="text-xs font-semibold text-accent-violet">
                #{chunk.rank}
              </span>
              <span className="text-xs text-slate-500">
                score {chunk.score.toFixed(3)}
              </span>
            </div>
            <p className="text-sm font-medium text-slate-200">{chunk.title}</p>
            <p className="text-xs text-accent-teal">{chunk.source_type}</p>
            <p className="mt-1 line-clamp-3 text-xs text-slate-400">
              {chunk.chunk_text}
            </p>
          </button>
        ))
      )}
    </div>
  );
}
