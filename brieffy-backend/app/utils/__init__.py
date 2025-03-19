from .jwt_handler import create_access_token, decode_access_token
from .srapper import Scraper
from .ai_text_processor import TextProcessor
from .embedder import embed_text
from .title import get_title

scrapper = Scraper()
text_processor = TextProcessor()

__all__ = ["create_access_token", "decode_access_token", "scrapper", "text_processor", "embed_text", "get_title"]