from pdf_reader import read_pdf

if __name__ == "__main__":
    pdf_path = "samples/test.pdf"  # change name if your pdf is different
    text = read_pdf(pdf_path)

    print("✅ PDF loaded successfully!")
    print("Characters extracted:", len(text))
    print("\n--- Preview (first 500 chars) ---\n")
    print(text[:500])
