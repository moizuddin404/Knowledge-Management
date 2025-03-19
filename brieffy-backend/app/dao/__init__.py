from .knowledge_card_dao import KnowledgeCardDao
from .user_dao import UserDAO

user_dao = UserDAO()


__all__ = ["user_dao", "KnowledgeCardDao"]

