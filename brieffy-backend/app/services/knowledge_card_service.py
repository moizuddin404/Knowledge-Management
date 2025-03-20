from utils import scrapper, text_processor, decode_access_token, embedder_for_title
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
            note = knowledge_card_data.note
            source_url = knowledge_card_data.source_url

            # Scrape content from the given URL
            content = scrapper.scrape_web(source_url)
            if not content:
                return None  

            # Extract and clean body content
            body_content = scrapper.extract_body_content(content)
            # print(body_content)
            cleaned_content = scrapper.clean_body_content(body_content)
            # print(cleaned_content)
            chunks = scrapper.split_content(cleaned_content)
            # print(chunks)

            summary = text_processor.summarize_text(chunks)
            # print("\nSummary", summary)
            # Extract title and process text
            title = text_processor.get_title(summary)
            print("\ntitle000000", title)
            # extract tags from suummary
            tags = text_processor.generate_tags(summary)
            print(tags)
            embedding = embedder_for_title.embed_text(title)
            print(embedding)

            # print(title, summary, tags, embedding)
            # Store knowledge card in the database
            card_data = knowledge_card_dao.insert_knowledge_card(
                user_id, title, summary, tags, note, embedding, source_url
            )
            return card_data

        except Exception as exception:
            print(f"Error processing knowledge card: {exception}")
            return None  
        
    def get_all_cards(self, token:str):
        """
        Usage: Retrieve all knowledge cards for a specific user.
        Parameters: token (str): The access token of the user whose cards are to be retrieved.
        Returns: list: A list of knowledge cards.
        """
        print("tokkennn", token)
        decoded_token = decode_access_token(token)
        print("printing decoded token00")
        print(decoded_token)
        user_id = decoded_token["userId"]

        all_cards = knowledge_card_dao.get_all_cards(user_id)

        card_details = []
        for card in all_cards:
            card_details.append({
                "title": card.title,
                "summary": card.summary,
                "note": card.note,
                "tags":card.tags,
                "source_url": card.source_url
            })
                
        return card_details
