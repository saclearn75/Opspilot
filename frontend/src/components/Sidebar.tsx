interface SidebarProps {
  onReadData: () => void;
  onClearData: () => void;
  readDisabled: boolean;
  loading: boolean;
}

export default function Sidebar({
  onReadData,
  onClearData,
  readDisabled,
  loading,
}: SidebarProps) {
  return (
    <aside className="flex w-44 shrink-0 flex-col gap-3 border-r border-surface-border bg-surface-raised p-4">
      <button
        type="button"
        onClick={onReadData}
        disabled={readDisabled || loading}
        className="rounded-lg bg-violet-500/20 px-4 py-3 text-sm font-medium text-accent-violet transition hover:bg-violet-500/30 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Read Data
      </button>
      <button
        type="button"
        onClick={onClearData}
        disabled={loading}
        className="rounded-lg bg-rose-500/20 px-4 py-3 text-sm font-medium text-accent-rose transition hover:bg-rose-500/30 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Clear Data
      </button>
    </aside>
  );
}
