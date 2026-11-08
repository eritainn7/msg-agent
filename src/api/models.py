from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone

class ChatMessage(BaseModel):
    message_id: UUID = Field(default_factory=uuid4)
    role: Literal["user", "assistant", "system"]
    content: str
    metadata: Optional[Dict[str, Any]] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ChatRequest(BaseModel):
    user_id: int
    session_id: UUID
    messages: List[ChatMessage]
    stream: bool = True
    platform: Optional[Literal["max", "vk", "telegram"]] = None
    account_id: Optional[str] = None

class HistoryResponse(BaseModel):
    session_id: UUID
    messages: List[ChatMessage]
    total: int