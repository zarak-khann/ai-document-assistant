from app.core.embeddings import EmbeddingModel
from app.core.vector_store import VectorStore


class Retriever:
    """Retrieve relevant document chunks for a query."""

    def __init__(
        self,
        vector_store: VectorStore | None = None,
        embedding_model: EmbeddingModel | None = None,
    ):
        self.embedding_model = embedding_model or EmbeddingModel()
        self.vector_store = vector_store or VectorStore()

    def retrieve(self, query: str, n_results: int = 3) -> dict:
        """Find the most relevant chunks for a query."""
        if not query.strip():
            raise ValueError("Query cannot be empty")

        query_embedding = self.embedding_model.embed_query(query)

        return self.vector_store.search(
            query_embedding=query_embedding,
            n_results=n_results,
        )