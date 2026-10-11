from app.rag.loader import load_pdf

from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore  

def create_document_ids(chunks):
    ids =[]

    for index, chunk in enumerate(chunks):
        source = chunk.metadata.get("source", "unknown")
        page = chunk.metadata.get("page", 0)

        chunk_id = f"{source}_page_{page}_chunk_{index}"
        ids.append(chunk_id)

    return ids


def index_documents(file_path):
    documents = load_pdf(file_path)
    chunks = split_documents(documents)
    ids = create_document_ids(chunks)
    vectorstore = create_vectorstore(chunks, ids)
    return vectorstore


if __name__ == "__main__":
    index_documents(r"D:\newfile\chatbot1\data\documents\pdf\RAG_Complete_Guide.pdf")