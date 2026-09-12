from pathlib import Path

from app.loaders.base import BaseDocumentLoader
from app.loaders.pdf_loader import PDFLoader
from app.loaders.docx_loader import DOCXLoader
from app.loaders.excel_loader import ExcelLoader
from app.loaders.text_loader import TextLoader

class DocumentLoaderFactory:
    """
    Creates the correct document loader based on file type.
    """

    _loaders = {
        ".pdf": PDFLoader,
        ".docx": DOCXLoader,
        ".xlsx": ExcelLoader,
        ".xlsm": ExcelLoader,
        ".txt": TextLoader,
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