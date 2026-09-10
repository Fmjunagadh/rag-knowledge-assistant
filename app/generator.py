import time

from google import genai

from app.config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_answer(
    question: str,
    documents: list[dict],
) -> dict:
    """
    Generate an answer using retrieved document chunks.

    Returns:
        {
            "answer": "...",
            "citations": [...]
        }
    """

    # ---------------------------------------------------------
    # 1. Build context for the LLM
    # ---------------------------------------------------------

    context_parts = []

    for document in documents:

        text = document.get("text", "")

        metadata = document.get("metadata", {})

        file_name = metadata.get(
            "file_name",
            "Unknown document"
        )

        page_number = metadata.get(
            "page",
            "Unknown"
        )

        context_parts.append(
            f"""
Source:
File: {file_name}
Page: {page_number}

Content:
{text}
"""
        )

    context = "\n\n".join(context_parts)

    # ---------------------------------------------------------
    # 2. Build prompt
    # ---------------------------------------------------------

    prompt = f"""
You are a helpful knowledge assistant.

Answer the user's question using only the information
provided in the context below.

If the answer cannot be found in the context, say:

"I don't have enough information in the provided documents."

Do not make up information.

Context:
{context}

User Question:
{question}

Answer:
"""

    # ---------------------------------------------------------
    # 3. Gemini models with fallback
    # ---------------------------------------------------------

    models = [
        "gemini-3.8-flash",
        "gemini-3.6-flash",
    ]

    # ---------------------------------------------------------
    # 4. Generate answer
    # ---------------------------------------------------------

    for model in models:

        print(f"🤖 Trying model: {model}")

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                answer = response.text

                # -------------------------------------------------
                # 5. Prepare citations
                # -------------------------------------------------

                citations = []

                for document in documents:

                    metadata = document.get(
                        "metadata",
                        {}
                    )

                    citation = {
                        "file_name": metadata.get(
                            "file_name"
                        ),
                        "page_number": metadata.get(
                            "page"
                        ),
                        "chunk_index": metadata.get(
                            "chunk_index"
                        ),
                    }

                    citations.append(citation)

                return {
                    "answer": answer,
                    "citations": citations,
                }

            except Exception as error:

                if "503" in str(error):

                    print(
                        f"⚠️ Model unavailable. "
                        f"Retry {attempt + 1}/3..."
                    )

                    time.sleep(2 ** attempt)

                else:

                    raise

        print(
            f"⚠️ Switching from {model}..."
        )

    return {
        "answer": (
            "Sorry, Gemini is currently unavailable. "
            "Please try again later."
        ),
        "citations": [],
    }