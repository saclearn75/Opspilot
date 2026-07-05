import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(PROJECT_ROOT / "backend" / ".env")

DATA_DIR = PROJECT_ROOT / "data"
SQLITE_PATH = PROJECT_ROOT / "backend" / "storage" / "memoryos.db"
CHROMA_PATH = PROJECT_ROOT / "backend" / "storage" / "chroma"

OPENAI_KEY = os.getenv("OPENAI_KEY")
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
TOP_K = 8
OPENAI_CHAT_MODEL = "gpt-4o-mini"
