from app.chatbot.prompt import RAG_PROMPT
from app.chatbot.memory import DatabaseMemory
from app.llm.model import get_response
from app.rag.retriever import get_retriever
from app.rag.reranker import rerank_documents


class Chatbot:

    def __init__(self, vectorstore):

        self.retriever = get_retriever(vectorstore)

        self.memory = DatabaseMemory()

    def chat(
        self,session_id,message):

        # Get previous conversation
        history = self.memory.get_history(session_id)

        # Save user message
        self.memory.add_message(session_id,"user",message)

        # Retrieve relevant documents
        documents = self.retriever.invoke(message)

        documents = rerank_documents(question=message,documents=documents,top_n=3)

        # Create document context
        context = "\n\n".join(document.page_content for document in documents)

        # Create prompt
        prompt = RAG_PROMPT.format(history=history,context=context,question=message)

        # Generate answer
        answer = get_response(prompt)

        # Save AI message
        self.memory.add_message(session_id,"assistant",answer)

        sources =[]

        for document in documents:
            source_path = document.metadata.get("source_path", "unknown")
            page = document.metadata.get("page", "unknown")

            source = {
                "source_path": source_path,
                "page": page + 1 if page is not None else "unknown"
            }
            if source not in sources:
                sources.append(source)

        return {
            "answer": answer,
            "sources": sources
        }