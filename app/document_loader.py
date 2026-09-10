from pathlib import Path

from pypdf import PdfReader

from app.models import DocumentChunk


def load_pdf(file_path: str) -> list[DocumentChunk]:
    """
    Load a PDF and convert each page into a normalized
    DocumentChunk object.
    """

    path = Path(file_path)

    reader = PdfReader(file_path)

    chunks = []

    chunk_index = 0

    for page_number, page in enumerate(reader.pages, start=1):

        page_text = page.extract_text()

        if not page_text or not page_text.strip():
            continue

        chunk_index += 1

        chunk = DocumentChunk(
            document_id=path.stem,
            file_name=path.name,
            content=page_text.strip(),
            page=page_number,
            section=None,
            chunk_index=chunk_index,
            file_type="pdf",
        )

        chunks.append(chunk)

    return chunks


    