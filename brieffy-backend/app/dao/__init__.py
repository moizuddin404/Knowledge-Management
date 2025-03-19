from .knowledge_card_dao import KnowledgeCardDao
from .user_dao import UserDAO

user_dao = UserDAO()
knowledge_card_dao = KnowledgeCardDao()

__all__ = ["user_dao", "knowledge_card_dao"]

