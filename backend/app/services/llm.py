from openai import OpenAI

from backend.app.config import OPENAI_CHAT_MODEL, OPENAI_KEY
from backend.app.schemas.ask import AskResponse, ChunkResult


def _get_openai_client() -> OpenAI:
    if not OPENAI_KEY:
        raise ValueError("OPENAI_KEY environment variable not set")
    return OpenAI(api_key=OPENAI_KEY)


def generate_answer(question: str, chunks: list[ChunkResult]) -> AskResponse:
    client = _get_openai_client()

    if not chunks:
        return AskResponse(
            answer="No relevant context was found in the knowledge base. Try reading data first or rephrasing your question.",
            chunks=[],
        )

    context_blocks = []
    for chunk in chunks:
        context_blocks.append(
            f"[{chunk.rank}] Title: {chunk.title}\n"
            f"Source: {chunk.source_type}\n"
            f"Content: {chunk.chunk_text}"
        )
    context_text = "\n\n".join(context_blocks)

    system_prompt = (
        "You are OpsPilot, an institutional memory assistant. "
        "Answer the user's question using only the provided context snippets. "
        "Cite source titles when relevant. If the context is insufficient, say so clearly."
    )
    user_prompt = f"Question: {question}\n\nContext:\n{context_text}"

    completion = client.chat.completions.create(
        model=OPENAI_CHAT_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
    )

    answer = completion.choices[0].message.content or ""
    return AskResponse(answer=answer, chunks=chunks)
