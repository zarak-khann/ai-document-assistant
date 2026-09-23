from app.core.retriever import Retriever


class FakeEmbeddingModel:
    def embed_query(self, query: str) -> list[float]:
        return [0.0, 1.0, 0.0]


class FakeVectorStore:
    def search(self, query_embedding: list[float], n_results: int) -> dict:
        assert query_embedding == [0.0, 1.0, 0.0]
        assert n_results == 1

        return {
            "documents": [["Artificial intelligence learns from data."]]
        }


def test_retrieve():
    retriever = Retriever(
        vector_store=FakeVectorStore(),
        embedding_model=FakeEmbeddingModel(),
    )

    results = retriever.retrieve(
        "How does artificial intelligence learn?",
        n_results=1,
    )

    assert results["documents"][0][0] == (
        "Artificial intelligence learns from data."
    )