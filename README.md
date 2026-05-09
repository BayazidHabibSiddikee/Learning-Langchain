# Mechatronics Sage: Advanced Hybrid RAG Ecosystem

This repository contains a comprehensive implementation of a Retrieval-Augmented Generation (RAG) system, specifically architected for the domain of **Mechatronics Engineering**. The system functions as an automated "Technical Sage," capable of pedagogical instruction, optimized code generation, and formal documentation.

## 🏗 System Architecture

The project follows a modular, step-by-step evolution (p1 through p11) that mirrors the standard RAG lifecycle, optimized for local execution on **Fedora Linux** using **Ollama**.

### 1. The Core Engine (`p1` - `p5`)

* **LLM Integration**: Initial configuration of local models via Ollama.
* **Prompt Engineering**: Development of complex templates including a 50-year veteran Mechatronics persona.
* **Structured Output**: Implementation of `Pydantic` and `JSON` output parsers to ensure type-safe responses for hardware and software specifications.
* **Chains**: Orchestration of logic using LangChain Expression Language (LCEL).

### 2. Knowledge Ingestion (`p6` - `p9`)

* **Document Loading**: Automated ingestion of multi-source PDF documentation (e.g., Control Systems and Mathematics literature).
* **Recursive Splitting**: Context-aware text chunking with 3000-character windows and 150-character overlaps to maintain mathematical continuity.
* **Hybrid Vector Storage**:
* **ChromaDB**: Utilized for persistent metadata management.
* **FAISS (CPU)**: Implemented for high-speed, in-memory semantic indexing of dense vector embeddings (`nomic-embed-text`).



### 3. Advanced Retrieval & Routing (`p10` - `p11`)

* **Ensemble Retrieval**: A hybrid search architecture combining BM25 (keyword-based) and Vector Similarity (semantic-based) using Reciprocal Rank Fusion (RRF).
* **Multi-Query Expansion**: Automated query generation to improve recall for complex engineering problems.
* **Intent-Based Routing**: A high-level `Review` model that classifies user input into four distinct operational modes:
* `learn`: Pedagogical breakdowns of control theory and math.
* `code`: Optimized firmware and systems programming (C++, Python).
* `lab`: Automated draft generation for experimental reports.
* `normal`: Fluid conversational interaction.



## 📂 Directory Structure

| File/Folder | Purpose |
| --- | --- |
| `RAG/p11.Final_RAG_SYSTEM.ipynb` | The integrated production-ready system with intent routing. |
| `p10.retrievers.ipynb` | Implementation of Ensemble and Multi-Query logic. |
| `p9.x_Faiss_CPU.ipynb` | High-performance semantic search indexing. |
| `p3.structured_output.py` | Pydantic schemas for engineering-grade JSON data. |
| `RAG/faiss_db/` | Local vector index for the engineering knowledge base. |
| `pdf/` | Source literature (Control Systems, Math for Programmers). |

## 🛠 Technical Stack

* **Framework**: LangChain (Core, Community, and Ollama)
* **Inference**: Ollama (`marin:latest`, `nomic-embed-text`)
* **Compute**: Local CPU-optimized FAISS (Fedora Linux)
* **Data Models**: Pydantic v2
* **Search Algorithms**: BM25 + Vector Cosine Similarity

## 🚀 Key Innovation: The Intent Classifier

Unlike static RAG systems, this architecture utilizes a **pre-processing classification layer**. Every user query is first analyzed by a `Review(BaseModel)` which determines the sentiment and technical requirements. This allows the system to switch between a string-based chat mode and a JSON-structured reporting mode dynamically, reducing token noise and increasing accuracy for hardware-level tasks.

---

*Built for the intersection of Hardware Reality and Systems Logic.*
