from pypdf import PdfReader

def read_pdf(file_path: str) -> str:
    """Read a PDF file and return extracted text as one string."""
    reader = PdfReader(file_path)
    
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text



