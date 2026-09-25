from app.core.llm import LLM
from app.core.rag import RAGPipeline
from app.core.retriever import Retriever
from app.ingestion.pipeline import IngestionPipeline


def test_end_to_end():
    # 1. Ingest the document
    ingestion = IngestionPipeline()

    count = ingestion.ingest(
        "data/uploads/test.txt",
        chunk_size=100,
        overlap=20,
    )

    assert count > 0

    # 2. Create the retriever
    retriever = Retriever()

    # 3. Create the LLM
    llm = LLM()

    # 4. Connect retrieval + LLM
    rag = RAGPipeline(
        retriever=retriever,
        llm=llm,
    )

    # 5. Ask a question
    answer = rag.answer(
        "What is this document about?"
    )

    assert isinstance(answer, dict)
    assert "answer" in answer
    assert "sources" in answer
    assert isinstance(answer["answer"], str)
    assert isinstance(answer["sources"], list)
    assert answer["answer"].strip()