from app.ingestion.loaders import load_pdf, load_txt


def test_load_txt():
    text = load_txt("data/uploads/test.txt")

    assert "Artificial intelligence" in text
    assert "Machine learning" in text


def test_load_pdf():
    pages = load_pdf("data/uploads/test.pdf")

    assert len(pages) > 0
    assert pages[0]["page_number"] == 1
    assert pages[0]["source"] == "test.pdf"
    assert pages[0]["text"]