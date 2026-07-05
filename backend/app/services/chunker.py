from typing import List, Tuple


def chunk_text(text: str, chunk_size: int, overlap: int) -> List[Tuple[str, int, int]]:
    chunks: List[Tuple[str, int, int]] = []
    start = 0
    step = max(chunk_size - overlap, 1)

    while start < len(text):
        end = min(start + chunk_size, len(text))
        raw = text[start:end]
        stripped = raw.strip()
        if stripped:
            lead = len(raw) - len(raw.lstrip())
            actual_start = start + lead
            actual_end = actual_start + len(stripped)
            chunks.append((stripped, actual_start, actual_end))
        start += step

    return chunks
