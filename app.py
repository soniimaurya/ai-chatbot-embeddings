import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os
import streamlit as st

# =========================
# 1. Crawl Website
# =========================
def crawl_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except:
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["header", "footer", "nav", "script", "style", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    return text


# =========================
# 2. Text Chunking
# =========================
def process_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)


# =========================
# 3. Embeddings + FAISS
# =========================
model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    return model.encode(chunks)

def save_embeddings(vectors, chunks):
    os.makedirs("data", exist_ok=True)

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    faiss.write_index(index, "data/index.faiss")

    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

def load_embeddings():
    index = faiss.read_index("data/index.faiss")
    with open("data/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)
    return index, chunks


# =========================
# 4. Question Answering (RAG)
# =========================
def answer_question(question):
    try:
        index, chunks = load_embeddings()
    except:
        return "❌ Please index a website first."

    q_vector = model.encode([question])
    D, I = index.search(q_vector, k=3)

    context = " ".join([chunks[i] for i in I[0]])

    if not context.strip():
        return "❌ Answer not found on website."

    return context[:500]


# =========================
# 5. Streamlit UI
# =========================
st.title("🌐 Website AI Chatbot (One File)")

url = st.text_input("Enter Website URL:")

if st.button("Index Website"):
    text = crawl_website(url)

    if text is None:
        st.error("❌ Invalid or unreachable URL.")
    else:
        chunks = process_text(text)
        vectors = create_embeddings(chunks)
        save_embeddings(vectors, chunks)
        st.success("✅ Website Indexed Successfully!")

question = st.text_input("Ask a question:")

if st.button("Ask"):
    answer = answer_question(question)
    st.write("🤖 Answer:", answer)
