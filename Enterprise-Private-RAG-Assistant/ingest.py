from app.ingestion.pdf_loader import load_pdf
from app.ingestion.embedder import Embedder
from app.ingestion.indexer import Indexer
from app.qdrant_db import initialize_collection


PDF_PATH = r"FAQ_of_Quant_Finance.pdf"


def main():

    # 1. init DB
    initialize_collection()

    # 2. load PDF
    pages = load_pdf(PDF_PATH)

    # 3. embedder
    embedder = Embedder()

    # 4. indexer
    indexer = Indexer(embedder)

    # 5. ingest
    indexer.index(pages)


if __name__ == "__main__":
    main()
