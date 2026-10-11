from fastapi import APIRouter
from pydantic import BaseModel
from app.database.connection import SessionLocal
from app.chatbot.bot import Chatbot
from app.rag.vectorstore import load_vectorstore
from app.database.chat import get_history, save_message


router = APIRouter()


class ChatRequest(BaseModel):

    session_id: str
    message: str

class source(BaseModel):
    
    source_path: str
    page: int | None = None

class ChatResponse(BaseModel):

    answer: str
    sources: list[source]


vectorstore = load_vectorstore()

chatbot = Chatbot(vectorstore)

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    db = SessionLocal()

    try:
        history = get_history(
            db,
            request.session_id
        )

        result = chatbot.chat(
            request.message,
            history
        )

        save_message(
            db,
            request.session_id,
            "user",
            request.message
        )

        save_message(
            db,
            request.session_id,
            "assistant",
            result["answer"]
        )

        return ChatResponse(**result)

    finally:
        db.close()