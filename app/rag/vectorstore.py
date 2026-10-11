from langchain_chroma import Chroma
from app.rag.embedding import get_embeddings

COLLECTION_NAME = "documents"

PERSIST_DIRECTORY = "data/processed/chroma"


def create_vectorstore(chunks,ids):
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        ids=ids,
        persist_directory=PERSIST_DIRECTORY,
        collection_name=COLLECTION_NAME
    )

    return vectorstore


def load_vectorstore():

    embeddings = get_embeddings()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    return vectorstore