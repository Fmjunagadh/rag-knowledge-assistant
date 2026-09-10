from app.models import DocumentChunk


def chunk_documents(
    documents: list[DocumentChunk],
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[DocumentChunk]:

    chunks = []

    global_chunk_index = 0

    for document in documents:

        content = document.content

        start = 0

        while start < len(content):

            end = start + chunk_size

            chunk_content = content[start:end].strip()

            if chunk_content:

                global_chunk_index += 1

                chunk = DocumentChunk(
                    document_id=document.document_id,
                    file_name=document.file_name,
                    content=chunk_content,
                    page=document.page,
                    section=document.section,
                    chunk_index=global_chunk_index,
                    file_type=document.file_type,
                )

                chunks.append(chunk)

            start += chunk_size - overlap

    return chunks