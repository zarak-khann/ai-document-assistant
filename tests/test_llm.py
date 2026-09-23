from app.core.llm import LLM


def test_generate():
    llm = LLM()

    response = llm.generate(
        "What is artificial intelligence? Answer in one sentence."
    )

    assert isinstance(response, str)
    assert response.strip()