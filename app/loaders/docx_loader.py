from pathlib import Path

from docx import Document

from app.loaders.base import BaseDocumentLoader
from app.models import DocumentChunk


class DOCXLoader(BaseDocumentLoader):
    """
    Loader for DOCX documents.
    """

    def load(
        self,
        file_path: str,
    ) -> list[DocumentChunk]:

        path = Path(file_path)

        document = Document(file_path)

        documents = []

        chunk_index = 0

        current_section = None

        for paragraph in document.paragraphs:

            text = paragraph.text.strip()

            if not text:
                continue

            # Detect headings
            if paragraph.style.name.startswith("Heading"):
                current_section = text
                continue

            chunk_index += 1

            chunk = DocumentChunk(
                document_id=path.stem,
                file_name=path.name,
                content=text,
                page=None,
                section=current_section,
                chunk_index=chunk_index,
                file_type="docx",
            )

            documents.append(chunk)

        return documents

        