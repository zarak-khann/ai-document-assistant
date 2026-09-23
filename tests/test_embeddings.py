from app.core.embeddings import EmbeddingModel


def test_embed_texts():
    model = EmbeddingModel()

    embeddings = model.embed_texts(
        [
            "Artificial intelligence learns from data.",
            "Python is a programming language.",
        ]
    )

    assert len(embeddings) == 2
    assert len(embeddings[0]) > 0
    assert len(embeddings[0]) == len(embeddings[1])


def test_embed_query():
    model = EmbeddingModel()

    embedding = model.embed_query("What is artificial intelligence?")

    assert len(embedding) > 0


def test_empty_texts():
    model = EmbeddingModel()

    assert model.embed_texts([]) == []