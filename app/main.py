from fastapi import FastAPI
from app.api.router import router

app = FastAPI( title="Document QA Chatbot")
app.include_router(router)
