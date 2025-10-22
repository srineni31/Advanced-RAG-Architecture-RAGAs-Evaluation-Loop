import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="RAG Observability Dashboard", layout="wide")

st.title("🔍 Advanced RAG Observability Dashboard")
st.markdown("""
This dashboard visualizes **retrieval performance**, **faithfulness metrics**, and **latency logs**
from your **RAG + RAGAs + TruLens** architecture.
""")

# Load metrics
latency_path = "results/latency_logs.csv"
ragas_path = "results/evaluation_metrics.json"

col1, col2 = st.columns(2)

if os.path.exists(latency_path):
    with col1:
        st.subheader("⚡ Retrieval & Response Latency")
        df = pd.read_csv(latency_path)
        st.line_chart(df.set_index(df.columns[0]))
else:
    st.warning("Latency logs not found. Run the pipeline to generate logs.")

if os.path.exists(ragas_path):
    with col2:
        st.subheader("📊 RAGAs Evaluation Metrics")
        with open(ragas_path, "r") as f:
            metrics = json.load(f)
        st.json(metrics)
else:
    st.info("No evaluation metrics found yet. Run your RAG pipeline to log them.")

st.markdown("---")
st.markdown("### 💬 Summary Insights") 
st.write("- Faithfulness and context recall indicate grounding strength.") 
st.write("- Latency spikes highlight retriever optimization opportunities.") 
st.write("- Aim for faithfulness >90% and latency <2s for production-grade RAG.")

st.markdown("---") 
st.caption("Built with ❤️ using Streamlit | LangChain | FAISS | RAGAs | TruLens") 
