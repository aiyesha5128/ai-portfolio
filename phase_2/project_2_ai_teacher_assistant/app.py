import os
import streamlit as st

from pdf_reader import read_pdf
from rag_engine import chunk_text, retrieve_relevant_chunks
from sk_orchestrator import run_prompt


def load_prompt(prompt_file: str) -> str:
    """Read a prompt template from prompts/ folder."""
    path = os.path.join("prompts", prompt_file)
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


st.set_page_config(page_title="AI Teacher Assistant", layout="centered")
st.title("📘 AI Teacher Assistant (Simple RAG + Semantic Kernel)")

st.write("Choose a PDF, select a mode (Answer/Summary/Quiz), and generate output.")

# --- PDF selection ---
st.subheader("1) Choose a PDF")

use_upload = st.checkbox("Upload a PDF instead of using samples", value=False)
pdf_path = None

if use_upload:
    uploaded = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded is not None:
        os.makedirs("outputs", exist_ok=True)
        pdf_path = os.path.join("outputs", uploaded.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded.read())
        st.success(f"Uploaded: {uploaded.name}")
else:
    sample_files = []
    if os.path.exists("samples"):
        sample_files = [f for f in os.listdir("samples") if f.lower().endswith(".pdf")]

    if not sample_files:
        st.warning("No PDFs found in the samples folder. Add a PDF to /samples.")
    else:
        selected = st.selectbox("Select a sample PDF", sample_files)
        pdf_path = os.path.join("samples", selected)

# --- Mode selection ---
st.subheader("2) Select Mode")

mode = st.radio("What do you want to generate?", ["Answer", "Summary", "Quiz"])

question = ""
if mode == "Answer":
    question = st.text_input("Enter the student's question")

top_k = st.slider("How many chunks to use as context?", 1, 5, 3)

# --- Run button ---
if st.button("Generate"):
    if not pdf_path:
        st.error("Please upload a PDF or select one from samples.")
        st.stop()

    if mode == "Answer" and not question.strip():
        st.error("Please enter a question.")
        st.stop()

    # Load prompt template based on mode
    if mode == "Answer":
        instruction = load_prompt("answer.txt")
        user_prompt = f"{instruction}\n\nStudent Question: {question}"
    elif mode == "Summary":
        instruction = load_prompt("summary.txt")
        user_prompt = instruction
    else:
        instruction = load_prompt("quiz.txt")
        user_prompt = instruction

    with st.spinner("Reading PDF..."):
        raw_text = read_pdf(pdf_path)

    if not raw_text.strip():
        st.error("No text could be extracted from this PDF. Try a different PDF.")
        st.stop()

    with st.spinner("Chunking + retrieving relevant context..."):
        chunks = chunk_text(raw_text, chunk_size=800, overlap=200)
        relevant = retrieve_relevant_chunks(chunks, user_prompt, top_k=top_k)
        context = "\n\n---\n\n".join(relevant)

    st.subheader("Retrieved Context (Transparency)")
    st.text_area("Top chunks used:", context, height=200)

    with st.spinner("Generating output..."):
        output = run_prompt(user_prompt, context)

    st.subheader("✅ Output")
    st.markdown(output)

