from utils.srapper import fetch_web_content
from utils.title import get_title
from utils.summarizer import summarize_text
from utils.tagger import generate_tags
from utils.embedder import embed_text
from dao.knowledge_card_dao import insert_knowledge_card

def process_knowledge_card(user_id: str, source_url: str, note: str):
    """Scrape content, get title, summarize, generate tags, embedd the title and store the knowledge card."""
    content = fetch_web_content(source_url)
    if not content:
        return None  
    title = get_title(content)
    summary = summarize_text(content)
    tags = generate_tags(summary)
    embedding = embed_text(summary)
    card_id = insert_knowledge_card(user_id, title, summary, tags, note, embedding, source_url)
    return card_id