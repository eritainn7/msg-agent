from fastapi import FastAPI
from models import ChatRequest, HistoryResponse
app = FastAPI()

@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    return "mock"

@app.get("/chat/history", response_model=HistoryResponse)
async def chat_history(user_id: str, session_id: str):
    return "mock"

@app.post("/chat/clear")
async def clear_history(user_id: str, session_id: str):
    return "mock"

@app.get("/health")
async def health():
    return {"status": "ok"}