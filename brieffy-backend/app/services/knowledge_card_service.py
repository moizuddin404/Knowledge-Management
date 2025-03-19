from utils import scrapper, text_processor, embed_text, get_title
from dao import KnowledgeCardDao

class KnowledgeCardService:
    def __init__(self, scrapper, text_processor, embed_text, knowledge_card_dao, get_title):
        """
        Initializes the KnowledgeCardService with required dependencies
        """
        self.scrapper = scrapper
        self.text_processor = text_processor
        self.embed_text = embed_text
        self.get_title = get_title
        self.knowledge_card_dao = knowledge_card_dao

    def process_knowledge_card(self, user_id: str, source_url: str, note: str):
        """
        Usage:Scrape content, get title, summarize, generate tags, embedd the title and store the knowledge card.
        Parameters:
            user_id (str): The ID of the user who owns this knowledge card
            source_url (str): The URL of the source content
            note (str): Additional notes about the content
        Returns:
            str: The ID of the inserted knowledge card
        """
        try:
            # Scrape content from the given URL
            content = self.scrapper.scrape_web(source_url)
            if not content:
                return None  

            # Extract and clean body content
            body_content = self.scrapper.extract_body_content(content)
            cleaned_content = self.scrapper.clean_body_content(body_content)

            # Extract title and process text
            title = self.get_title(cleaned_content)
            summary = self.text_processor.summarize_text(cleaned_content)
            tags = self.text_processor.generate_tags(summary)
            embedding = self.embed_text(title)

            print(title, summary, tags, embedding)
            # Store knowledge card in the database
            card_id, card_title = self.knowledge_card_dao.insert_knowledge_card(
                user_id, title, summary, tags, note, embedding, source_url
            )
            return card_id, card_title

        except Exception as exception:
            print(f"Error processing knowledge card: {exception}")
            return None  
        
        
