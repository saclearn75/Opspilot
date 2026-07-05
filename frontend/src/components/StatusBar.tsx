interface StatusBarProps {
  message: string;
  isError: boolean;
}

export default function StatusBar({ message, isError }: StatusBarProps) {
  return (
    <footer
      className={`border-t border-surface-border px-4 py-2 text-sm ${
        isError ? "text-red-400" : "text-slate-400"
      }`}
    >
      {message || "Ready"}
    </footer>
  );
}
