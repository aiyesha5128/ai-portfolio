from rag_engine import chunk_text, retrieve_relevant_chunks

if __name__ == "__main__":
    text = (
        "Artificial intelligence is transforming education. "
        "Students use AI tools to understand complex topics. "
        "Teachers can create quizzes and summaries using AI. "
        "Machine learning is a subset of artificial intelligence."
    )

    chunks = chunk_text(text, chunk_size=50, overlap=10)

    print("Total chunks:", len(chunks))
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:\n{chunk}")

    query = "What is artificial intelligence?"
    relevant = retrieve_relevant_chunks(chunks, query)

    print("\nTop relevant chunks:")
    for chunk in relevant:
        print("-", chunk)
