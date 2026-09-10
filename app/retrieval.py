from app.embeddings import create_embedding
from app.vector_store import search


def retrieve_documents(
    query: str,
    n_results: int = 3,
):

    query_embedding = create_embedding(
        query
    )

    results = search(
        query_embedding,
        n_results=n_results,
    )

    documents = results.get(
        "documents",
        [[]],
    )[0]

    metadatas = results.get(
        "metadatas",
        [[]],
    )[0]

    distances = results.get(
        "distances",
        [[]],
    )[0]

    retrieved_documents = []

    for index, document in enumerate(
        documents
    ):

        metadata = metadatas[index]

        distance = distances[index]

        retrieved_documents.append(
            {
                "text": document,
                "metadata": metadata,
                "distance": distance,
            }
        )

    return retrieved_documents