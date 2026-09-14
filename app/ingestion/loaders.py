from pathlib import Path
from docx import Document

import fitz

from app.models.schemas import DocumentPage


def load_txt(file_path: str) -> list[DocumentPage]:
    """Read a TXT file and return it as a document page."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        text = file.read().strip()

    return [
        DocumentPage(
            text=text,
            source=path.name,
        )
    ]


def load_pdf(file_path: str) -> list[DocumentPage]:
    """Extract text from a PDF page by page."""
    path = Path(file_path)
    pages = []

    with fitz.open(path) as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()

            pages.append(
                DocumentPage(
                    text=text,
                    source=path.name,
                    page_number=page_number,
                )
            )

    return pages




def load_docx(file_path: str) -> list[DocumentPage]:
    """Read a DOCX file and return its text as a document page."""
    path = Path(file_path)
    document = Document(path)

    text = "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ).strip()

    return [
        DocumentPage(
            text=text,
            source=path.name,
        )
    ]