from .jwt_handler import create_access_token, decode_access_token
from .srapper import Scraper
from .ai_text_processor import TextProcessor
from .embedder import Embedder
from .custom_exceptions import DatabaseError, NotFoundError

scrapper = Scraper()
text_processor = TextProcessor()
embedder_for_title = Embedder()

__all__ = ["create_access_token", "decode_access_token", "scrapper", "text_processor", "get_title", "embedder_for_title"]