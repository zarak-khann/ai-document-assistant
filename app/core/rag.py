from app.core.llm import LLM
from app.core.retriever import Retriever


class RAGPipeline:
    """Connect retrieval with LLM-based answer generation."""

    def __init__(
        self,
        retriever: Retriever,
        llm: LLM,
    ):
        self.retriever = retriever
        self.llm = llm

    def answer(self, question: str, n_results: int = 3) -> dict:
        """Answer a question and return the answer with its sources."""
        if not question.strip():
            raise ValueError("Question cannot be empty")

        results = self.retriever.retrieve(
            query=question,
            n_results=n_results,
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            return {
                "answer": "I could not find relevant information in the documents.",
                "sources": [],
            }

        context = "\n\n".join(documents)

        prompt = f"""
Answer the question using only the provided context.
If the answer is not present in the context, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{question}

Answer:
""".strip()

        answer = self.llm.generate(prompt)

        return {
            "answer": answer,
            "sources": metadatas,
        }