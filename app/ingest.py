from pathlib import Path

from app.document_loader import load_pdf
from app.chunker import chunk_text
from app.embeddings import create_embedding
from app.vector_store import add_documents


PDF_PATH = Path("data/documents/company_policy.pdf")


def ingest_document():
    print("📄 Loading document...")

    text = load_pdf(str(PDF_PATH))

    print(f"Extracted {len(text)} characters.")

    print("✂️ Creating chunks...")

    chunks = chunk_text(text)

    print(f"Created {len(chunks)} chunks.")

    print("🧠 Creating embeddings...")

    embeddings = []

    for index, chunk in enumerate(chunks, start=1):
        print(f"Embedding chunk {index}/{len(chunks)}...")

        embedding = create_embedding(chunk)

        embeddings.append(embedding)

    print("💾 Storing data in ChromaDB...")

    add_documents(chunks, embeddings)

    print("✅ Document ingestion completed successfully!")


if __name__ == "__main__":
    ingest_document()