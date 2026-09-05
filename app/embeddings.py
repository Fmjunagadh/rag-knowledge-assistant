from google import genai

from app.config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)


def create_embedding(text: str):
    """
    Generate an embedding vector for the supplied text.
    """

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )

    return response.embeddings[0].values


if __name__ == "__main__":
    text = "Employees are entitled to 20 days of annual leave."

    embedding = create_embedding(text)

    print("Embedding created successfully!")
    print("Vector dimensions:", len(embedding))
    print("First 10 values:", embedding[:10])