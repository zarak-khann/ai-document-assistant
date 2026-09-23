import pytest

from app.ingestion.cleaner import clean_text, validate_text


def test_clean_text():
    raw_text = "  Hello    world \r\n\r\n\r\n This is a test.  "

    cleaned = clean_text(raw_text)

    assert cleaned == "Hello world\n\nThis is a test."



def test_clean_text_preserves_paragraphs():
    raw_text = "First paragraph.\n\nSecond paragraph."

    assert clean_text(raw_text) == raw_text


def test_validate_text_accepts_meaningful_text():
    validate_text("Artificial intelligence is useful.")


def test_validate_text_rejects_empty_text():
    with pytest.raises(ValueError):
        validate_text("   ")


def test_validate_text_rejects_non_string():
    with pytest.raises(TypeError):
        validate_text(None)