from bson import ObjectId
from datetime import datetime
from database.mongodb import knowledge_cards_collection

def insert_knowledge_card(user_id: str, title: str, summary: str, tags: list, note: str, embedding: list, source_url: str, created_at: str):
    """Insert a knowledge card into MongoDB."""
    knowledge_card = {
        "userID": ObjectId(user_id),
        "Title": title,
        "Summary": summary,
        "Tags": tags,
        "Note": note,
        "CreatedAt": datetime.utcnow().isoformat(),
        "EmbeddedVector": embedding,
        "SourceURL": source_url
    }
    result = knowledge_cards_collection.insert_one(knowledge_card)
    return str(result.inserted_id)