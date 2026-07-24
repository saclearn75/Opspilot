from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app.db.chroma import get_or_create_collection
from backend.app.db.sqlite import init_db
from backend.app.routes import ask, clear, documents, ingest, status
from backend.app.schemas.common import ErrorResponse, HealthResponse

import os

app = FastAPI(title="OpsPilot API", root_path=os.getenv("ROOT_PATH",""))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(status.router, prefix="/api", tags=["status"])
app.include_router(ingest.router, prefix="/api", tags=["ingest"])
app.include_router(clear.router, prefix="/api", tags=["clear"])
app.include_router(ask.router, prefix="/api", tags=["ask"])
app.include_router(documents.router, prefix="/api", tags=["documents"])


@app.on_event("startup")
async def startup_event() -> None:
    init_db()
    get_or_create_collection()


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(error="Internal Server Error", detail=str(exc)).model_dump(),
    )


@app.get("/api/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return HealthResponse(status="ok")
