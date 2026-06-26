from app.embeddings import EmbeddingModel


class Embedder:
    def __init__(self):
        self.model = EmbeddingModel()

    def embed(self, text: str):
        return self.model.encode(text)
