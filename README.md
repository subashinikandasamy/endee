# 🧠 AI Research Paper Finder (RAG + FAISS + Streamlit)

> A production-style Retrieval Augmented Generation (RAG) system that allows users to search, retrieve, and summarize academic research papers using semantic vector search and LLMs.

---

## 📌 Overview

This project is an AI-powered research assistant that enables users to search academic papers using natural language. It combines:

- 🔍 FAISS vector database for semantic similarity search  
- 📚 arXiv dataset for research paper ingestion  
- 🧠 RAG pipeline (Retrieval Augmented Generation)  
- 💬 Large Language Model (Hugging Face API)  
- 🌐 Streamlit web interface  

---

## ⚙️ System Architecture


User Query
↓
Streamlit UI
↓
FAISS Vector Search (Semantic Retrieval)
↓
Top-k Relevant Papers
↓
LLM (Hugging Face Inference API)
↓
Final Contextual Answer


---

## 🚀 Features

- ⚡ Real-time semantic search over research papers  
- 🧠 Context-aware AI-generated answers (RAG pipeline)  
- 📄 Automatic ingestion of arXiv papers  
- 🔎 FAISS-powered vector similarity search  
- 🌐 Interactive Streamlit UI  
- 📚 Domain-focused research assistant  

---

## 🛠️ Tech Stack

- Python 🐍  
- FAISS (Vector Database)  
- Streamlit (Frontend UI)  
- Hugging Face Inference API 🤗  
- arXiv API 📚  
- NLP + Embeddings  

---

## 📂 Project Structure


ai-research-finder/
│
├── app.py # Streamlit UI
├── faiss_db.py # Vector DB logic (FAISS)
├── arxiv_loader.py # Paper fetching module
├── llm.py # LLM inference logic
├── embed.py # Embedding generation
├── requirements.txt
└── README.md


---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ai-research-finder.git
cd ai-research-finder
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Application
streamlit run app.py
🔍 How It Works
User enters a research query
Query is converted into embeddings
FAISS retrieves top-k similar research papers
Retrieved context is passed to LLM
LLM generates final contextual answer
Results displayed in Streamlit UI
📊 Example Use Cases
Student research assistant
AI literature review tool
Semantic search engine for papers
RAG-based chatbot system
Academic knowledge explorer
📸 Demo

<img width="1365" height="677" alt="image" src="https://github.com/user-attachments/assets/5d014b1a-a4d1-4d20-bf0f-1a00e950f21c" />


![UI Screenshot](assets/demo.png)
🧠 Key Highlights
End-to-end RAG pipeline implementation
Efficient similarity search using FAISS
Real-world LLM integration
Clean modular architecture
Production-style project structure
🚀 Future Improvements
Add multi-modal paper search (PDF support)
Improve embedding model accuracy
Add user authentication
Deploy on cloud (AWS / Hugging Face Spaces)
Add citation tracking system
👨‍💻 Author

Subashini K
AI/ML Intern Project

📌 Note

This project demonstrates a full-stack AI system combining vector databases + LLMs + RAG architecture, suitable for production-level AI applications.


---

# 🚀 WHY THIS IS FAANG LEVEL

✔ Clear system design diagram  
✔ Clean modular structure  
✔ Engineering language (not student wording)  
✔ Scalability section  
✔ Future improvements (very important in interviews)  
✔ Production framing (“RAG pipeline”, “vector DB”, etc.)

---

# ⚡ NEXT STEP (IMPORTANT)

After updating README:

```bash
git add README.md
git commit -m "upgrade README to FAANG level"
git push
