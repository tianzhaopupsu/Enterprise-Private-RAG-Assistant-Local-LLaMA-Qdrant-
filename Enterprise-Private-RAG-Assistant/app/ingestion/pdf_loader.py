import os

import fitz  # PyMuPDF


def load_pdf(file_path: str):
    doc = fitz.open(file_path)
    file_name = os.path.basename(file_path)
    pages = []

    for i, page in enumerate(doc):
        text = page.get_text("text")
        pages.append({
            "page": i + 1,
            "text": text,
            "source": file_name
        })

    return pages
