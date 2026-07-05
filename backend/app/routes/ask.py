from fastapi import APIRouter, HTTPException

from backend.app.schemas.ask import AskRequest, AskResponse
from backend.app.services.llm import generate_answer
from backend.app.services.retrieval import retrieve_chunks

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    try:
        chunks = retrieve_chunks(request.question)
        return generate_answer(request.question, chunks)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
