from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    # -------------------------
    # Qdrant
    # -------------------------
    QDRANT_HOST = os.getenv(
        "QDRANT_HOST",
        "127.0.0.1"
    )

    QDRANT_PORT = int(
        os.getenv(
            "QDRANT_PORT",
            6333
        )
    )

    COLLECTION_NAME = os.getenv(
        "COLLECTION_NAME",
        "scientific_rag"
    )

    # -------------------------
    # Embedding Model
    # -------------------------
    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    # -------------------------
    # Local LLM
    # -------------------------
    BASE_MODEL = os.getenv(
        "BASE_MODEL",
        "meta-llama/Llama-3.2-3B"
    )


settings = Settings()
