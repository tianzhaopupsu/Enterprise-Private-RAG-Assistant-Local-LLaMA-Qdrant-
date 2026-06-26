from qdrant_client import QdrantClient
from qdrant_client.models import QueryRequest
from sentence_transformers import SentenceTransformer
from app.setting import settings


class Retriever:
    def __init__(self):
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

        self.encoder = SentenceTransformer("BAAI/bge-small-en-v1.5")
        self.collection = settings.COLLECTION_NAME

    def retrieve(self, query, top_k=5):
        vector = self.encoder.encode(query).tolist()

        results = self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=top_k
        ).points

        return [
            {
                "text": r.payload.get("text", ""),
                "page": r.payload.get("page", -1),
                "source": r.payload.get("source", "unknown"),
                "score": r.score,
                "payload": r.payload  # Safe structural fallback flag for your UI
            }
            for r in results
        ]
