
from dotenv import load_dotenv

import os

load_dotenv()

CHROMA_DB = os.getenv(
    "CHROMA_DB",
    "./chroma_db"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "BAAI/bge-m3"
)

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1"
)

LLM_PROVIDER = "ollama"

OLLAMA_MODEL = "qwen2.5:7b"

OLLAMA_URL = "http://localhost:11434"
