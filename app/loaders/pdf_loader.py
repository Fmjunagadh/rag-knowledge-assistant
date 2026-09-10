from pathlib import Path

from pypdf import PdfReader

from app.loaders.base import BaseDocumentLoader
from app.models import DocumentChunk


class PDFLoader(BaseDocumentLoader):
    """
    Loader for PDF documents.
    """

    def load(
        self,
        file_path: str,
    ) -> list[DocumentChunk]:

        path = Path(file_path)

        reader = PdfReader(file_path)

        documents = []

        chunk_index = 0

        for page_number, page in enumerate(
            reader.pages,
            start=1,
        ):

            page_text = page.extract_text()

            if not page_text or not page_text.strip():
                continue

            chunk_index += 1

            document = DocumentChunk(
                document_id=path.stem,
                file_name=path.name,
                content=page_text.strip(),
                page=page_number,
                section=None,
                chunk_index=chunk_index,
                file_type="pdf",
            )

            documents.append(document)

        return documents
        