import json
from sentence_transformers import SentenceTransformer, util
import openai

model = SentenceTransformer("all-MiniLM-L6-v2")
openai.api_key = "YOUR_OPENAI_API_KEY"

def load_data(path):
    with open(path, 'r') as f:
        return json.load(f)

def get_relevant_chunks(question, docs, top_k=3):
    question_emb = model.encode(question, convert_to_tensor=True)
    doc_embeddings = [model.encode(doc['text'], convert_to_tensor=True) for doc in docs]
    scores = [float(util.pytorch_cos_sim(question_emb, emb)) for emb in doc_embeddings]
    sorted_docs = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
    return [doc for _, doc in sorted_docs[:top_k]]

def generate_answer(question, contexts):
    context_text = "\n---\n".join([doc['text'] for doc in contexts])
    prompt = f"Answer the question based on the context below:\n{context_text}\n\nQuestion: {question}\nAnswer:"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}]
    )
    return res['choices'][0]['message']['content'].strip()
