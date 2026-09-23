from app.ingestion.pipeline import IngestionPipeline


def test_ingestion_pipeline():
    pipeline = IngestionPipeline()

    count = pipeline.ingest(
        "data/uploads/test.txt",
        chunk_size=100,
        overlap=20,
    )

    assert count > 0