def chunk_text(text, chunk_size=800, overlap=200):
    """
    Split text into overlapping chunks.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks


def retrieve_relevant_chunks(chunks, query, top_k=3):
    """
    Retrieve top-k relevant chunks using keyword overlap.
    """
    scored = []
    query_words = set(query.lower().split())

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(query_words.intersection(chunk_words))
        scored.append((score, chunk))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [chunk for score, chunk in scored[:top_k]]
