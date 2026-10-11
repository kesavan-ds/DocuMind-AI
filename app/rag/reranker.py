

from sentence_transformers import CrossEncoder


MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

reranker_model = CrossEncoder(MODEL_NAME)


def rerank_documents(question, documents, top_n=3):

    if not documents:
        return []

    pairs = [
        (question, document.page_content)
        for document in documents
    ]

    scores = reranker_model.predict(pairs)

    ranked_documents = sorted(
        zip(documents, scores),
        key=lambda item: float(item[1]),
        reverse=True
    )

    return [
        document
        for document, score in ranked_documents[:top_n]
    ]
