from fastapi import APIRouter, HTTPException
from models import KnowledgeCardRequest, KnowledgeCardResponse
from services import  knowledge_card_service
from utils import decode_access_token

knowledge_card_router = APIRouter()

@knowledge_card_router.post("/")
async def add_knowledge_card(data:KnowledgeCardRequest):
    """API endpoint to add a knowledge card."""
    decoded_token = decode_access_token(data.token)
    userId = decoded_token["userId"]

    card_data = knowledge_card_service.process_knowledge_card(
        user_id=userId, source_url=data.source_url, note=data.note
        )

    if not card_data:
        raise HTTPException(status_code=400, detail="Failed to process knowledge card")
    
    # card_id, title = card_data
    # return KnowledgeCardResponse(
    #     message="Knowledge Card Added",
    #     knowledgeCardId=card_id,
    #     title=title
    # )
    return card_data
    
