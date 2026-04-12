# ---------------- CLEAN LOGGING ----------------
import os
import logging
import streamlit as st

os.environ["TRANSFORMERS_VERBOSITY"] = "error"
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

# ---------------- IMPORTS ----------------
from faiss_db import VectorDB
from arxiv_loader import fetch_papers
from llm import generate_answer

# ---------------- SETUP ----------------
db = VectorDB()

st.set_page_config(page_title="AI Research Finder", layout="wide")

st.title("🧠 AI Research Paper Finder (RAG + FAISS)")
st.caption("Retrieval-Augmented Generation (RAG) System using FAISS Vector Database + arXiv Research Data")

# ---------------- LOAD PAPERS ----------------
if st.button("📥 Load Papers"):
    papers = fetch_papers("machine learning", 20)

    for p in papers:
        db.add(p["title"] + " " + p["summary"])

    st.success(f"{len(papers)} Papers loaded successfully!")

# ---------------- USER INPUT ----------------
query = st.text_input("🔍 Ask something about research papers:")

# ---------------- RESULTS ----------------
if query:

    results = db.search(query)

    if not results:
        st.warning("No results found. Click 'Load Papers' first.")
        st.stop()

    # SAFE context building
    context = "\n".join(results)

    # AI Answer (safe call)
    try:
        answer = generate_answer(context, query)
    except Exception as e:
        answer = f"AI Error: {str(e)}"

    st.markdown("## 🤖 AI Answer")
    st.success(answer)

    st.markdown("## 📄 Similar Research Papers")

    for r in results:
        st.markdown("---")
        st.write(r[:400] + "...")
        st.caption("🧠 Retrieved using FAISS semantic search")
