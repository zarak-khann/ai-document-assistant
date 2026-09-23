import pytest

from app.ingestion.chunker import chunk_text


def test_chunk_text():
    text = "abcdefghijklmnopqrstuvwxyz"

    chunks = chunk_text(text, chunk_size=10, overlap=2)

    assert len(chunks) == 4
    assert chunks[0] == "abcdefghij"
    assert chunks[1] == "ijklmnopqr"
    assert chunks[2] == "qrstuvwxyz"


def test_chunk_text_empty():
    assert chunk_text("   ") == []


def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=0)


def test_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=10, overlap=10)