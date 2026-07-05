import chromadb
import os
from pathlib import Path

from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

from backend.app.config import CHROMA_PATH

_embedding_function = DefaultEmbeddingFunction()


def get_embedding_function() -> DefaultEmbeddingFunction:
    return _embedding_function


def get_chroma_client():
    chroma_path = Path(CHROMA_PATH)
    os.makedirs(chroma_path, exist_ok=True)
    return chromadb.PersistentClient(path=str(chroma_path))


def get_or_create_collection():
    client = get_chroma_client()
    return client.get_or_create_collection(
        name="chunks",
        embedding_function=get_embedding_function(),
    )


def clear_chroma_collection():
    client = get_chroma_client()
    try:
        client.delete_collection(name="chunks")
    except Exception:
        pass
    get_or_create_collection()
