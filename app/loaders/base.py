from abc import ABC, abstractmethod

from app.models import DocumentChunk


class BaseDocumentLoader(ABC):
    """
    Common interface for all document loaders.
    """

    @abstractmethod
    def load(
        self,
        file_path: str,
    ) -> list[DocumentChunk]:
        """
        Load a document and return normalized DocumentChunk objects.
        """
        pass