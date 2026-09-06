import time

from google import genai

from app.config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_answer(question: str, documents: list[str]) -> str:
    """
    Generate an answer using retrieved document chunks.
    """

    context = "\n\n".join(documents)

    prompt = f"""
You are a helpful knowledge assistant.

Answer the user's question using only the information provided
in the context below.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided documents."

Context:
{context}

User Question:
{question}

Answer:
"""

    models = [
        "gemini-3.8-flash",
        "gemini-3.6-flash",
    ]

    for model in models:

        print(f"🤖 Trying model: {model}")

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )

                return response.text

            except Exception as error:

                if "503" in str(error):

                    print(
                        f"⚠️ Model unavailable. "
                        f"Retry {attempt + 1}/3..."
                    )

                    time.sleep(2 ** attempt)

                else:
                    raise

        print(f"⚠️ Switching from {model}...")

    return "Sorry, Gemini is currently unavailable. Please try again later."