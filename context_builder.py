def build_context(retrieved_docs):
    return "\n".join([doc.page_content for doc in retrieved_docs])
