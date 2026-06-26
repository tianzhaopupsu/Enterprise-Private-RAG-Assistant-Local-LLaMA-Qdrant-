from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from app.setting import settings
from loguru import logger

client = QdrantClient(
    host=settings.QDRANT_HOST,
    port=settings.QDRANT_PORT
)


def initialize_collection(vector_size=384):
    collections = client.get_collections()

    existing = [
        c.name
        for c in collections.collections
    ]

    if settings.COLLECTION_NAME not in existing:

        logger.info(
            f"Creating collection: "
            f"{settings.COLLECTION_NAME}"
        )

        client.create_collection(
            collection_name=settings.COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE
            )
        )

    logger.info("Qdrant ready")
