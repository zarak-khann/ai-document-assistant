import re


def clean_text(text: str) -> str:
    """Clean and normalize extracted document text."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def validate_text(text: str) -> None:
    """Validate that text contains meaningful content."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.strip():
        raise ValueError("Document text cannot be empty")