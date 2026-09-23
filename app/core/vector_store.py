import chromadb


class VectorStore:
    """Store and search document embeddings using Chroma."""

    def __init__(self, path: str = "data/chroma"):
        self.client = chromadb.PersistentClient(path=path)

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(
        self,
        texts: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
        ids: list[str],
    ) -> None:
        """Store document chunks and their embeddings."""
        if not texts:
            return

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

    def search(
        self,
        query_embedding: list[float],
        n_results: int = 3,
    ) -> dict:
        """Find the most similar document chunks."""
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )