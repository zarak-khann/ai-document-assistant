from pathlib import Path
import hashlib

from app.core.embeddings import EmbeddingModel
from app.core.vector_store import VectorStore
from app.ingestion.cleaner import clean_text, validate_text
from app.ingestion.chunker import chunk_text
from app.ingestion.loaders import load_docx, load_pdf, load_txt


class IngestionPipeline:
    """Load, clean, chunk, embed, and store a document."""

    def __init__(
        self,
        embedding_model: EmbeddingModel | None = None,
        vector_store: VectorStore | None = None,
    ):
        self.embedding_model = embedding_model or EmbeddingModel()
        self.vector_store = vector_store or VectorStore()

    def load_document(self, file_path: str):
        """Select the correct loader based on file extension."""
        extension = Path(file_path).suffix.lower()

        if extension == ".txt":
            return load_txt(file_path)

        if extension == ".pdf":
            return load_pdf(file_path)

        if extension == ".docx":
            return load_docx(file_path)

        raise ValueError(f"Unsupported file type: {extension}")

    def ingest(
        self,
        file_path: str,
        chunk_size: int = 500,
        overlap: int = 50,
    ) -> int:
        """Process and store one document. Return number of chunks stored."""
        pages = self.load_document(file_path)

        chunks = []
        metadatas = []
        ids = []

        for page in pages:
            validate_text(page.text)
            cleaned_text = clean_text(page.text)

            page_chunks = chunk_text(
                cleaned_text,
                chunk_size=chunk_size,
                overlap=overlap,
            )

            for chunk_index, chunk in enumerate(page_chunks):
                chunks.append(chunk)

                metadata = {
                    "source": page.source,
                    "chunk_index": chunk_index,
                }

                if page.page_number is not None:
                    metadata["page_number"] = page.page_number

                chunk_id = hashlib.sha256(
                    f"{page.source}|{page.page_number}|"
                    f"{chunk_index}|{chunk}".encode("utf-8")
                ).hexdigest()

                metadatas.append(metadata)
                ids.append(chunk_id)

        if not chunks:
            return 0

        embeddings = self.embedding_model.embed_texts(chunks)

        self.vector_store.add_documents(
            texts=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

        return len(chunks)