from app.core.vector_store import VectorStore


def test_add_and_search():
    store = VectorStore(path="data/test_chroma")

    texts = [
        "Python is a programming language.",
        "Artificial intelligence learns from data.",
    ]

    embeddings = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
    ]

    metadatas = [
        {"source": "python.txt"},
        {"source": "ai.txt"},
    ]

    ids = ["python-1", "ai-1"]

    store.add_documents(
        texts=texts,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )

    results = store.search(
        query_embedding=[0.0, 1.0, 0.0],
        n_results=1,
    )

    assert results["documents"][0][0] == "Artificial intelligence learns from data."