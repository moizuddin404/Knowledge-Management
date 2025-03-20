from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
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
    return JSONResponse({ "message": "Knowledge card '{card_data}' added successfully" })

@knowledge_card_router.get("/")
async def get_knowledge_card(token:str):
    """API endpoint to get all cards of the user"""
    print(token)
    all_cards = knowledge_card_service.get_all_cards(token)
    return all_cards
    
