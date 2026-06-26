import uuid
from qdrant_client.models import PointStruct

from app.qdrant_db import client
from app.setting import settings


class Indexer:

    def __init__(self, embedder):
        self.embedder = embedder

    def index(self, pages):

        points = []

        for page in pages:

            chunks = self._chunk(page["text"])

            for chunk in chunks:

                vector = self.embedder.embed(chunk)

                # ---- FIX 1: ensure list format ----
                if hasattr(vector, "tolist"):
                    vector = vector.tolist()

                points.append(
                    PointStruct(
                        id=str(uuid.uuid4()),
                        vector=vector,
                        payload={
                            "text": chunk,
                            "page": page.get("page", -1),

                            # ---- FIX 2: ADD SOURCE ----
                            "source": page.get("source", "pdf_book")

                        }
                    )
                )

        # ---- optional safety ----
        if len(points) == 0:
            print("No chunks to index.")
            return

        client.upsert(
            collection_name=settings.COLLECTION_NAME,
            points=points
        )

        print(f"Inserted {len(points)} chunks")

    def _chunk(self, text):
        from app.ingestion.chunker import chunk_text
        return chunk_text(text)
