from fastapi import APIRouter, HTTPException
from models import KnowledgeCardRequest, KnowledgeCardResponse
from utils import decode_access_token
from services import knowledge_card_service

knowledge_card_router = APIRouter()

@knowledge_card_router.post("/")
async def add_knowledge_card(knowledge_card_data:KnowledgeCardRequest):
    """API endpoint to add a knowledge card."""    
    card_data = knowledge_card_service.process_knowledge_card(knowledge_card_data)

    if not card_data:
        raise HTTPException(status_code=400, detail="Failed to process knowledge card")
    
    # card_id, title = card_data
    # return KnowledgeCardResponse(
    #     message="Knowledge Card Added",
    #     knowledgeCardId=card_id,
    #     title=title
    # )
    return card_data
    
