from dataclasses import dataclass
from typing import Optional


@dataclass
class DocumentChunk:
    document_id: str
    file_name: str
    content: str
    page: Optional[int]
    section: Optional[str]
    chunk_index: int
    file_type: str