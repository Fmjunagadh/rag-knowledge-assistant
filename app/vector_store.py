import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def add_documents(
    chunks,
    embeddings,
):

    ids = [
        f"{chunk.document_id}_chunk_{chunk.chunk_index:04d}"
        for chunk in chunks
    ]

    documents = [
        chunk.content
        for chunk in chunks
    ]

    metadatas = [
        {
            "document_id": chunk.document_id,
            "file_name": chunk.file_name,
            "page": chunk.page if chunk.page is not None else -1,
            "section": (
                chunk.section
                if chunk.section is not None
                else ""
            ),
            "chunk_index": chunk.chunk_index,
            "file_type": chunk.file_type,
        }
        for chunk in chunks
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
    )


def search(
    query_embedding,
    n_results=3,
):

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        include=[
            "documents",
            "metadatas",
            "distances",
        ],
    )