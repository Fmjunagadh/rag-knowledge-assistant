from pathlib import Path

from app.loaders.factory import DocumentLoaderFactory
from app.chunker import chunk_documents
from app.embeddings import create_embedding
from app.vector_store import add_documents


def ingest_document(document_path: str):

    path = Path(document_path)

    # -----------------------------------------
    # 1. Validate file
    # -----------------------------------------

    if not path.exists():
        print(f"❌ File not found: {path}")
        return

    if not path.is_file():
        print(f"❌ Not a file: {path}")
        return

    print(f"\n📄 Document: {path.name}")

    # -----------------------------------------
    # 2. Get correct loader automatically
    # -----------------------------------------

    try:

        loader = DocumentLoaderFactory.get_loader(
            str(path)
        )

    except ValueError as error:

        print(f"❌ {error}")
        return

    print(
        f"Using loader: {type(loader).__name__}"
    )

    # -----------------------------------------
    # 3. Load document
    # -----------------------------------------

    print("\n📖 Loading document...")

    documents = loader.load(
        str(path)
    )

    print(
        f"Loaded {len(documents)} normalized documents."
    )

    if not documents:
        print("❌ No content found in document.")
        return

    # -----------------------------------------
    # 4. Create chunks
    # -----------------------------------------

    print("\n✂️ Creating chunks...")

    chunks = chunk_documents(
        documents
    )

    print(
        f"Created {len(chunks)} chunks."
    )

    if not chunks:
        print("❌ No chunks created.")
        return

    # -----------------------------------------
    # 5. Create embeddings
    # -----------------------------------------

    print("\n🧠 Creating embeddings...")

    embeddings = []

    for index, chunk in enumerate(
        chunks,
        start=1,
    ):

        print(
            f"Embedding chunk "
            f"{index}/{len(chunks)}..."
        )

        embedding = create_embedding(
            chunk.content
        )

        embeddings.append(
            embedding
        )

    # -----------------------------------------
    # 6. Store in ChromaDB
    # -----------------------------------------

    print("\n💾 Storing data in ChromaDB...")

    add_documents(
        chunks,
        embeddings,
    )

    print(
        "\n✅ Document ingestion completed!"
    )


if __name__ == "__main__":

    print("🤖 RAG Document Ingestion")

    documents_folder = Path("data/documents")

    if not documents_folder.exists():
        print(
            f"❌ Documents folder not found: "
            f"{documents_folder}"
        )

    else:

        print(
            f"\n📁 Scanning: "
            f"{documents_folder}/"
        )

        supported_extensions = {
            ".pdf",
            ".docx",
            ".xlsx",
            ".xlsm",
            ".txt",
        }

        files = [
            file
            for file in documents_folder.iterdir()
            if file.is_file()
            and file.suffix.lower()
            in supported_extensions
        ]

        if not files:
            print(
                "❌ No supported documents found."
            )

        else:

            print(
                f"\n📚 Found {len(files)} "
                f"supported documents."
            )

            for file in files:

                print("\n" + "=" * 60)

                ingest_document(
                    str(file)
                )

            print("\n" + "=" * 60)

            print(
                "\n🎉 All documents processed!"
            )