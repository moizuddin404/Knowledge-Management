from bson import ObjectId
from datetime import datetime
from database import db_instance
from models import KnowledgeCard

class KnowledgeCardDao:
    def __init__(self):
        """        
        Initialize the KnowledgeCardDao with a reference to the knowledge cards collection.
        """
        self.knowledge_cards_collection = db_instance.get_collection("knowledge_cards_collection")

    def insert_knowledge_card(self, user_id: str, title: str, summary: str, tags: list, note: str, embedding: list, source_url: str):
        """
        Usage:Insert a knowledge card into MongoDB"
        Parameters:
            user_id (str): The ID of the user who owns this knowledge card
            title (str): The title of the knowledge card
            summary (str): A summary of the content
            tags (list): A list of tags associated with the content
            note (str): Additional notes about the content
            embedding (list): Vector representation of the title for semantic search
            source_url (str): Original source URL of the content
        Returns:
            str: The ID of the inserted knowledge card
        """
        knowledge_card = {
            "userID": ObjectId(user_id),
            "title": title,
            "summary": summary,
            "tags": tags,
            "note": note,
            "createdAt": datetime.utcnow().isoformat(),
            "embeddedVector": embedding,
            "sourceURL": source_url
        }
        self.knowledge_cards_collection.insert_one(knowledge_card)
        return title
    
    def get_all_cards(self,user_id:str):
        """
        Usage: Retrieve all knowledge cards for a specific user.
        Parameters: user_id (str): The ID of the user whose cards are to be retrieved.
        Returns: list: A list of knowledge cards.
        """
        cards = self.knowledge_cards_collection.find({"userID": ObjectId(user_id)})

        return [
            KnowledgeCard(
                user_id=str(card["userID"]),
                title=card.get("title", ""),
                summary=card.get("summary", ""),
                tags=card.get("tags", []),
                note=card.get("note", ""),
                created_at=card.get("createdAt", ""),
                embedded_vector=card.get("embeddedVector", []),
                source_url=card.get("sourceURL", "")
            )
            for card in cards
        ]