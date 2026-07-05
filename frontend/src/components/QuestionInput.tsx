import type { KeyboardEvent } from "react";

interface QuestionInputProps {
  value: string;
  onChange: (value: string) => void;
  onSubmit: () => void;
  disabled: boolean;
}

export default function QuestionInput({
  value,
  onChange,
  onSubmit,
  disabled,
}: QuestionInputProps) {
  const handleKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "Enter" && !disabled) {
      event.preventDefault();
      onSubmit();
    }
  };

  return (
    <div className="flex gap-3">
      <input
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={disabled}
        placeholder="Ask a demo question..."
        className="flex-1 rounded-lg border border-surface-border bg-surface-raised px-4 py-2 text-slate-100 placeholder:text-slate-500 focus:border-violet-400/50 focus:outline-none disabled:opacity-50"
      />
      <button
        type="button"
        onClick={onSubmit}
        disabled={disabled || !value.trim()}
        className="rounded-lg bg-teal-500/20 px-6 py-2 font-medium text-accent-teal transition hover:bg-teal-500/30 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Submit
      </button>
    </div>
  );
}
