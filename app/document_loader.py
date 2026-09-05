from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


if __name__ == "__main__":
    pdf_path = Path("data/documents/company_policy.pdf")

    text = load_pdf(str(pdf_path))

    print("PDF loaded successfully!")
    print("-" * 50)
    print(text)