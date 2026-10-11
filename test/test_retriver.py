from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.vectorstore import create_vectorstore
from chatbot1.app.rag.retriever import get_retriver

documents = load_pdf(
    "D:\\newfile\\chatbot1\\data\\documents\\pdf\\RAG_Complete_Guide.pdf"
)
chunks = split_documents(documents)
vectorstore = create_vectorstore(chunks)
retriever = get_retriver(vectorstore)

results = retriever.invoke(
    "what is RAG?"      )

for result in results:
    print("\n--- RESULT ---")
    print("\n")
    print(result.page_content)
    print("\n")
    print(result.metadata)