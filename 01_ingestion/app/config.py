# app/config.py

from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CHROMA_DB_DIR = Path(__file__).resolve().parent.parent / "embeddings"