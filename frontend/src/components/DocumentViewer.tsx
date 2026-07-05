import { useEffect, useMemo, useRef } from "react";
import type { DocumentResponse } from "../types/api";

interface DocumentViewerProps {
  document: DocumentResponse | null;
}

export default function DocumentViewer({ document }: DocumentViewerProps) {
  const highlightRef = useRef<HTMLElement>(null);

  const highlightedBody = useMemo(() => {
    if (!document) {
      return null;
    }

    const { body, chunks, highlight_chunk_id } = document;
    if (!highlight_chunk_id) {
      return { type: "plain" as const, text: body };
    }

    const target = chunks.find((c) => c.chunk_id === highlight_chunk_id);
    if (!target) {
      return { type: "plain" as const, text: body };
    }

    return {
      type: "highlight" as const,
      before: body.slice(0, target.char_start),
      focus: body.slice(target.char_start, target.char_end),
      after: body.slice(target.char_end),
    };
  }, [document]);

  useEffect(() => {
    highlightRef.current?.scrollIntoView({ behavior: "smooth", block: "center" });
  }, [document?.highlight_chunk_id]);

  return (
    <div className="min-h-48 rounded-lg border border-surface-border bg-surface-raised p-4">
      {document ? (
        <>
          <div className="mb-3 border-b border-surface-border pb-2">
            <h3 className="text-base font-semibold text-accent-violet">
              {document.title}
            </h3>
            <p className="text-xs text-slate-500">
              {document.source_type} · {document.project} · {document.date}
            </p>
          </div>
          <pre className="whitespace-pre-wrap font-sans text-sm leading-relaxed text-slate-300">
            {highlightedBody?.type === "plain" ? (
              highlightedBody.text
            ) : highlightedBody?.type === "highlight" ? (
              <>
                {highlightedBody.before}
                <mark ref={highlightRef} className="chunk-highlight">
                  {highlightedBody.focus}
                </mark>
                {highlightedBody.after}
              </>
            ) : null}
          </pre>
        </>
      ) : (
        <p className="text-sm text-slate-500">
          Click a chunk card to view the full source document...
        </p>
      )}
    </div>
  );
}
