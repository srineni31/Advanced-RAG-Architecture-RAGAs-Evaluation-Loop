from retriever import HybridRetriever
from context_builder import build_context
from llm_generator import generate_answer
from evaluation_ragas import run_ragas_evaluation
from observability_trulens import TruLensObserver

def main():
    query = input("Enter your query: ")

    retriever = HybridRetriever()
    retrieved_docs = retriever.retrieve(query)

    context = build_context(retrieved_docs)
    answer = generate_answer(context)

    metrics = run_ragas_evaluation([answer], [context], [context])

    observer = TruLensObserver()
    observer.track(answer)

    print("\n=== Answer ===\n", answer)
    print("\n=== RAGAs Metrics ===\n", metrics)

if __name__ == "__main__":
    main()
