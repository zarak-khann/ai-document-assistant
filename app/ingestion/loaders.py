from pathlib import Path
import fitz


def load_txt(file_path: str) -> str:
    """Read a TXT file and return its text."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        return file.read()


def load_pdf(file_path: str) -> list[dict]:
    """Extract text from a PDF page by page."""
    path = Path(file_path)
    pages = []

    with fitz.open(path) as document:
        for page_number, page in enumerate(document, start=1):
            text = page.get_text("text").strip()

            pages.append(
                {
                    "text": text,
                    "page_number": page_number,
                    "source": path.name,
                }
            )

    return pages