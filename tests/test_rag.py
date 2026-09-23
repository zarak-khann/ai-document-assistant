from app.core.rag import RAGPipeline


class FakeRetriever:
    def retrieve(self, query: str, n_results: int) -> dict:
        return {
            "documents": [
                [
                    "Python is a programming language.",
                    "Python is commonly used in artificial intelligence.",
                ]
            ]
        }


class FakeLLM:
    def generate(self, prompt: str) -> str:
        assert "Python is a programming language." in prompt
        assert "What is Python?" in prompt

        return "Python is a programming language."


def test_rag_pipeline():
    pipeline = RAGPipeline(
        retriever=FakeRetriever(),
        llm=FakeLLM(),
    )

    answer = pipeline.answer("What is Python?", n_results=2)

    assert answer == "Python is a programming language."


def test_empty_question():
    pipeline = RAGPipeline(
        retriever=FakeRetriever(),
        llm=FakeLLM(),
    )

    try:
        pipeline.answer("   ")
        assert False
    except ValueError:
        assert True