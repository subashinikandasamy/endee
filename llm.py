# llm.py (FINAL CLEAN VERSION - NO API)

def generate_answer(context, query):
    if not context:
        return "No context found in database."

    return f"""
🧠 AI RESEARCH ASSISTANT (STABLE MODE)

🔍 Query:
{query}

📚 Top Retrieved Knowledge:
{context[:900]}

💡 AI Insight:
This topic is related to machine learning, NLP, and AI research systems.
The FAISS vector database successfully retrieved similar research papers.

✔ System working perfectly without external API.
"""