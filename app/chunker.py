from pathlib import Path

from app.document_loader import load_pdf


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50):
    """
    Split text into chunks with a small overlap between chunks.
    """

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    pdf_path = Path("data/documents/company_policy.pdf")

    text = load_pdf(str(pdf_path))

    chunks = chunk_text(text)

    print(f"Total chunks: {len(chunks)}")

    for index, chunk in enumerate(chunks, start=1):
        print("\n" + "=" * 60)
        print(f"CHUNK {index}")
        print("=" * 60)
        print(chunk)