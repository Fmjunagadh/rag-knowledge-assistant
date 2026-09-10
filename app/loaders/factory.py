from pathlib import Path

from app.loaders.base import BaseDocumentLoader
from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DOCXLoader


class DocumentLoaderFactory:
    """
    Creates the correct document loader based on file type.
    """

    _loaders = {
        ".pdf": PDFLoader,
        ".docx": DOCXLoader,
    }

    @classmethod
    def get_loader(
        cls,
        file_path: str,
    ) -> BaseDocumentLoader:

        extension = Path(
            file_path
        ).suffix.lower()

        loader_class = cls._loaders.get(
            extension
        )

        if not loader_class:

            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return loader_class()
