from fastapi import APIRouter
from pydantic import BaseModel
import ollama

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: list[Message]

@router.post("")
async def chat_with_ai(request: ChatRequest):
    response = ollama.chat(
        model="llama3",
        messages=[{"role": m.role, "content": m.content} for m in request.messages]
    )
    return {"response": response['message']['content']}
