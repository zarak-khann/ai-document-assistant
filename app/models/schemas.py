from dataclasses import dataclass


@dataclass
class DocumentPage:
    text: str
    source: str
    page_number: int | None = None