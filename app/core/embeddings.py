from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """Create vector embeddings for text."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Convert multiple texts into embeddings."""
        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embeddings.tolist()

    def embed_query(self, query: str) -> list[float]:
        """Convert one query into an embedding."""
        if not query.strip():
            raise ValueError("Query cannot be empty")

        embedding = self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        return embedding.tolist()