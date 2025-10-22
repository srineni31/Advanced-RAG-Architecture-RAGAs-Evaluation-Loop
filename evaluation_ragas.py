from ragas import evaluate

def run_ragas_evaluation(predictions, contexts, references):
    metrics = evaluate(
        predictions=predictions,
        references=references,
        contexts=contexts,
        metrics=["faithfulness", "context_recall", "answer_relevance"]
    )
    return metrics
