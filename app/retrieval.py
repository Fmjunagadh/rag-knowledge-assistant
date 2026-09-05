from app.embeddings import create_embedding
from app.vector_store import search


def retrieve_documents(query: str, n_results: int = 3):
    """
    Find the most relevant document chunks for a user query.
    """

    # Convert the user's question into an embedding
    query_embedding = create_embedding(query)

    # Search ChromaDB
    results = search(
        query_embedding,
        n_results=n_results,
    )

    documents = results.get("documents", [[]])[0]

    return documents


if __name__ == "__main__":

    print("🔎 RAG Retrieval")
    print("Type 'exit' to quit.")

    while True:

        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        documents = retrieve_documents(question)

        print("\n📚 Relevant Documents")
        print("=" * 60)

        if not documents:
            print("No relevant documents found.")
            continue

        for index, document in enumerate(documents, start=1):
            print(f"\n--- Result {index} ---")
            print(document)