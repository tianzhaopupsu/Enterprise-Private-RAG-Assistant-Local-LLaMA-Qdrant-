import os
import fitz
import camelot


# ===========================
# PDF Quality Assessment
# ===========================
def pdf_quality_score(doc):
    total_chars = 0
    empty_pages = 0
    image_pages = 0

    for page in doc:
        text = page.get_text("text").strip()
        total_chars += len(text)

        if not text:
            empty_pages += 1

        if page.get_images():
            image_pages += 1

    n_pages = max(len(doc), 1)
    avg_chars = total_chars / n_pages

    score = 1.0

    if avg_chars < 300:
        score -= 0.30
    if empty_pages / n_pages > 0.30:
        score -= 0.40
    if image_pages / n_pages > 0.50:
        score -= 0.20

    return max(score, 0.0)


# ===========================
# Layout Detection
# ===========================
def has_complex_layout(doc):
    for page in doc:
        try:
            blocks = page.get_text("blocks")

            if len(blocks) > 60:
                return True

            if page.get_images() and len(blocks) < 5:
                return True

        except Exception:
            continue

    return False


# ===========================
# TEXT extraction (PyMuPDF)
# ===========================
def extract_text_fitz(file_path):
    doc = fitz.open(file_path)
    file_name = os.path.basename(file_path)

    pages = []

    try:
        for i, page in enumerate(doc):
            text = page.get_text("text").strip()

            if not text:
                continue

            pages.append({
                "page": i + 1,
                "text": text,
                "source": file_name,
                "type": "text",
                "parser": "fitz"
            })

    finally:
        doc.close()

    return pages


# ===========================
# TABLE extraction (Camelot)
# ===========================
def extract_tables_camelot(file_path):
    file_name = os.path.basename(file_path)

    try:
        tables = camelot.read_pdf(file_path, pages="all", flavor="stream")
    except Exception as e:
        print(f"[Camelot Error] {e}")
        return []

    table_chunks = []

    for i, table in enumerate(tables):
        df = table.df

        # Convert table → RAG-friendly text
        table_text = "\n".join([
            " | ".join(row) for row in df.values
        ])

        table_chunks.append({
            "page": table.page,
            "text": f"[TABLE]\n{table_text}",
            "source": file_name,
            "type": "table",
            "parser": "camelot"
        })

    return table_chunks


# ===========================
# MAIN LOADER (Hybrid)
# ===========================
def load_pdf(file_path):

    doc = fitz.open(file_path)

    try:
        quality = pdf_quality_score(doc)
        complex_layout = has_complex_layout(doc)

        print(f"Quality Score : {quality:.2f}")
        print(f"Complex Layout: {complex_layout}")

    finally:
        doc.close()

    # 1. TEXT
    text_pages = extract_text_fitz(file_path)

    # 2. TABLES (Camelot)
    table_pages = extract_tables_camelot(file_path)

    # 3. MERGE
    all_chunks = text_pages + table_pages

    return all_chunks
