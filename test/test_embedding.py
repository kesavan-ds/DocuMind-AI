from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore


documents = load_pdf(
    "D:\\newfile\\chatbot1\\data\\documents\\pdf\\RAG_Complete_Guide.pdf"
)

chunks = split_documents(documents)

vectorstore = create_vectorstore(chunks)

results = vectorstore.similarity_search(
    "what is RAG?",
    k=3
)

for result in results:
    print("\n--- RESULT ---")
    print("\n")
    print(result.page_content)
    print("\n")
    print(result.metadata)