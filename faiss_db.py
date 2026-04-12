from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorDB:
    def __init__(self):
        self.texts = []
        self.index = faiss.IndexFlatL2(384)

    def add(self, text):
        vec = model.encode([text])[0]
        self.index.add(np.array([vec]).astype("float32"))
        self.texts.append(text)

    def search(self, query, k=5):
        if len(self.texts) == 0:
            return []

        vec = model.encode([query])
        D, I = self.index.search(np.array(vec).astype("float32"), k)

        results = []
        for i in I[0]:
            if i < len(self.texts):
                results.append(self.texts[i])

        return results