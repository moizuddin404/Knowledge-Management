from pydantic import BaseModel
from datetime import datetime

class KnowledgeCard(BaseModel):
    user_id: str
    title: str
    summary: str
    tags: list
    note: str
    created_at: datetime
    embedded_vector: list
    source_url: str

class KnowledgeCardRequest(BaseModel):
    token: str
    source_url: str
    note: str

class KnowledgeCardResponse(BaseModel):
    message: str
    knowledge_card_id: str
    title: str

