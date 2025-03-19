from pydantic import BaseModel, EmailStr

class KnowledgeCardRequest(BaseModel):
    userId: str
    sourceURL: EmailStr
    note: str

class KnowledgeCardResponse(BaseModel):
    message: str
    knowledgeCardId: str

