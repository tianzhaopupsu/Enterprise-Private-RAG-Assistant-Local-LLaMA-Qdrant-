from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer, CrossEncoder
from app.setting import settings


class Retriever:
    def __init__(self):
        self.client = QdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT
        )

        # embedding model (bi-encoder)
        self.encoder = SentenceTransformer("BAAI/bge-small-en-v1.5")

        # reranker (cross-encoder)
        self.reranker = CrossEncoder("BAAI/bge-reranker-base")

        self.collection = settings.COLLECTION_NAME

    def retrieve(self, query, top_k=5, fetch_k=20):

        # 1. embed query
        vector = self.encoder.encode(query).tolist()

        # 2. retrieve more candidates
        results = self.client.query_points(
            collection_name=self.collection,
            query=vector,
            limit=fetch_k
        ).points

        if not results:
            return []

        # 3. prepare reranking pairs
        pairs = [
            (query, r.payload.get("text", ""))
            for r in results
        ]

        scores = self.reranker.predict(pairs)

        # 4. attach rerank scores
        reranked = sorted(
            zip(results, scores),
            key=lambda x: x[1],
            reverse=True
        )

        # 5. return top_k
        return [
            {
                "text": r.payload.get("text", ""),
                "page": r.payload.get("page", -1),
                "source": r.payload.get("source", "unknown"),
                "score": float(score),
                "payload": r.payload
            }
            for r, score in reranked[:top_k]
        ]
