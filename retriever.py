from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.retrievers import BM25Retriever
import yaml

class HybridRetriever:
    def __init__(self, config_path="config/retriever_config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.embeddings = HuggingFaceEmbeddings(model_name=self.config['embedding_model'])
        self.faiss_store = FAISS.load_local("data/embeddings/faiss_index", self.embeddings)

    def retrieve(self, query, top_k=5):
        dense_results = self.faiss_store.similarity_search(query, top_k)
        sparse_results = BM25Retriever.from_texts([r.page_content for r in dense_results]).get_relevant_documents(query)
        return dense_results + sparse_results
