from google import genai

from app.config import GEMINI_API_KEY


def main():
    client = genai.Client(api_key=GEMINI_API_KEY)

    print("🤖 RAG Knowledge Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=user_message,
        )

        print(f"AI: {response.text}\n")


if __name__ == "__main__":
    main()