import chromadb


# Create a local ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")


# Create or get our collection
collection = client.get_or_create_collection(
    name="knowledge_base"
)


def add_documents(chunks, embeddings):
    """
    Store document chunks and their embeddings in ChromaDB.
    """

    ids = [f"chunk-{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings,
    )


def search(query_embedding, n_results=3):
    """
    Search ChromaDB for the most relevant chunks.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
    )

    return results


if __name__ == "__main__":
    print("ChromaDB initialized successfully!")
    print("Collection:", collection.name)