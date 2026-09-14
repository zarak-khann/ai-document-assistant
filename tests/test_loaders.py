from app.ingestion.loaders import load_docx, load_pdf, load_txt


def test_load_txt():
    pages = load_txt("data/uploads/test.txt")

    assert len(pages) == 1
    assert "Artificial intelligence" in pages[0].text
    assert pages[0].source == "test.txt"
    assert pages[0].page_number is None


def test_load_pdf():
    pages = load_pdf("data/uploads/test.pdf")

    assert len(pages) > 0
    assert pages[0].page_number == 1
    assert pages[0].source == "test.pdf"
    assert pages[0].text


def test_load_docx():
    pages = load_docx("data/uploads/test.docx")

    assert len(pages) == 1
    assert "We propose" in pages[0].text
    assert pages[0].source == "test.docx"
    assert pages[0].page_number is None