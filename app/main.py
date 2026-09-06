from app.retrieval import retrieve_documents
from app.generator import generate_answer


def main():
    print("🤖 RAG Knowledge Assistant")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            print("Please enter a question.")
            continue

        print("\n🔎 Searching knowledge base...")

        documents = retrieve_documents(question)

        if not documents:
            print("\n❌ No relevant information found.")
            continue

        print(f"📚 Retrieved {len(documents)} relevant chunks.")

        print("\n🧠 Generating answer...")

        answer = generate_answer(
            question,
            documents
        )

        print("\n🤖 Answer")
        print("=" * 60)
        print(answer)


if __name__ == "__main__":
    main()