from utils import scrapper, text_processor, embed_text, get_title, decode_access_token
from models import KnowledgeCardRequest
from dao import knowledge_card_dao

class KnowledgeCardService:
    # def __init__(self, scrapper, text_processor, embed_text, knowledge_card_dao, get_title):
    #     """
    #     Initializes the KnowledgeCardService with required dependencies
    #     """
    #     self.scrapper = scrapper
    #     self.text_processor = text_processor
    #     self.embed_text = embed_text
    #     self.get_title = get_title
    #     self.knowledge_card_dao = knowledge_card_dao

    def process_knowledge_card(self, knowledge_card_data: KnowledgeCardRequest):
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
            decoded_token = decode_access_token(knowledge_card_data.token)
            user_id = decoded_token["userId"]
            # Scrape content from the given URL
            content = scrapper.scrape_web(knowledge_card_data.source_url)
            if not content:
                return None  

            # Extract and clean body content
            body_content = scrapper.extract_body_content(content)
            print(body_content)
            cleaned_content = scrapper.clean_body_content(body_content)
            print(cleaned_content)
            chunks = scrapper.split_content(cleaned_content)
            print(chunks)

            # Extract title and process text
            title = get_title()
            print("\ntitle", title)
            summary = text_processor.summarize_text(chunks)
            print("\nSummary", summary)
            tags = text_processor.generate_tags(summary)
            embedding = embed_text()

            print(title, summary, tags, embedding)
            # Store knowledge card in the database
            card_id, card_title = knowledge_card_dao.insert_knowledge_card(
                user_id, title, summary, tags, knowledge_card_data.note, embedding, knowledge_card_data.source_url
            )
            return card_id, card_title

        except Exception as exception:
            print(f"Error processing knowledge card: {exception}")
            return None  
        
        
