from pathlib import Path

from app.loaders.base import BaseDocumentLoader
from app.models import DocumentChunk


class TextLoader(BaseDocumentLoader):
    """
    Loader for TXT documents.
    """

    def load(
        self,
        file_path: str,
    ) -> list[DocumentChunk]:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if path.suffix.lower() != ".txt":
            raise ValueError(
                f"Unsupported file type: {path.suffix}"
            )

        text = path.read_text(
            encoding="utf-8"
        )

        if not text.strip():
            return []

        chunk = DocumentChunk(
            document_id=path.stem,
            file_name=path.name,
            content=text.strip(),
            page=None,
            section=None,
            chunk_index=1,
            file_type="txt",
        )

        return [chunk]