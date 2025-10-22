# Advanced RAG Architecture + RAGAs Evaluation Loop

This repository demonstrates an **enterprise-grade Retrieval-Augmented Generation (RAG)** pipeline with **Monitoring, Observability, and Evaluation**.

### 🔍 Features
- Hybrid Retriever (BM25 + FAISS)
- Context Builder for dynamic document merging
- RAGAs-based evaluation (Faithfulness, Context Recall, Answer Relevance)
- TruLens monitoring with latency, quality, and hallucination detection
- Cost-free implementation (no external APIs)

### 🧠 Architecture Flow
User Query → Hybrid Retriever → Context Builder → LLM → RAGAs Evaluation → Metrics Loop

### 📊 Observability Metrics
- Retrieval Latency < 2s  
- Context Utilization 85–95%  
- Answer Accuracy ≥ 90%  
- Faithfulness tracked with RAGAs  

### ⚙️ Stack
Python | LangChain | FAISS | Hugging Face | RAGAs | TruLens | Streamlit (optional UI)

### 🚀 Quick Start
```bash
git clone https://github.com/yourusername/advanced-rag-observability.git
cd advanced-rag-observability
pip install -r requirements.txt
python src/main.py
