interface LlmOutputProps {
  answer: string;
}

export default function LlmOutput({ answer }: LlmOutputProps) {
  return (
    <textarea
      readOnly
      value={answer || "LLM answer will appear here..."}
      className="h-64 w-full resize-none rounded-lg border border-surface-border bg-surface-raised p-4 text-sm leading-relaxed text-slate-200 focus:outline-none"
    />
  );
}
