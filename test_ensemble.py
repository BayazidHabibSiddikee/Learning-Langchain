import subprocess
import os

# Start ollama serve
subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import time
time.sleep(3)

from langchain_classic.retrievers.ensemble import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 0. Load docs - use absolute path since we run from langchain/ not RAG/
rag_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RAG")
loader = PyPDFDirectoryLoader(path=os.path.join(rag_dir, "doc"), glob="**/*.pdf")
docs = loader.load()
print(f"Loaded {len(docs)} docs")

# 1. Split
rec_split = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n"], chunk_size=3000, chunk_overlap=150
).split_documents(docs)
print(f"Split into {len(rec_split)} chunks")

# 2. Initialize Sparse Retriever (Keyword-based)
print("\nCreating BM25 retriever...")
bm25_retriever = BM25Retriever.from_documents(rec_split)
bm25_retriever.k = 4

# 3. Initialize Dense Retriever (Semantic-based)
print("Creating FAISS + Ollama embeddings...")
embed = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_documents(rec_split, embed)
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# 4. Combine with Ensemble Retriever
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vectorstore_retriever],
    weights=[0.3, 0.7]  # Weights define importance
)

# 5. Test it
print("\n=== Testing Ensemble Retriever ===")
query = "How does the model learn?"
results = ensemble_retriever.invoke(query)
print(f"Query: '{query}'")
print(f"Results found: {len(results)}")
for i, doc in enumerate(results):
    print(f"\n── Result {i+1} (page {doc.metadata.get('page','?')}) ──")
    print(doc.page_content[:300])