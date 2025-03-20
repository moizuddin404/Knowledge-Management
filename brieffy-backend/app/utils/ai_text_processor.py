from openai import OpenAI
import os
from dotenv import load_dotenv
from config import Config
import re

class TextProcessor:
    
    
    def generate_tags(self, content, max_tags=5):
        """
        Usage:Generate tags from the provided content.
        Parameters:
        - content (str): The content to generate tags for
        - max_tags (int): Maximum number of tags to generate
        Returns:
        - str: Generated tags
        """
        base_url = Config.OPEN_API_BASE
        api_key = Config.OPEN_API_KEY

        client = OpenAI(
            base_url= base_url,
            api_key= api_key
        )
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "user",
                    "content": f"""Generate tags for following content:\n\n
                    {content}\n\n
                    ### Tagging Guidelines:
                    1. Provide tags that accurately describe the content.
                    2. Include only major topics and keywords.
                    3. Avoid duplicates.
                    4. Only give top {max_tags} tags.
                    5. Return the tags as a **comma-separated list** (e.g., AI, Machine Learning, Deep Learning).

                    """
                }
            ]
        )
        tags = completion.choices[0].message.content.strip()

        # Split by commas and remove any surrounding spaces
        tags_list = [tag.strip() for tag in tags.replace("\n", "").split(",") if tag.strip()]  

        return tags_list
    
    
    
    
    def summarize_text(self, chunks):
        """
        Usage: Summarize text chunks and optionally save to a file.
        Parameters:
        - chunks (list): List of text chunks to summarize
        - output_file (str, optional): Path to save the summarized output
        Returns:
        - str: Combined summary of all chunks
        """
        base_url = Config.OPEN_API_BASE
        api_key = Config.OPEN_API_KEY

        client = OpenAI(
            base_url= base_url,
            api_key= api_key
        )
        summarized_data = []
        for chunk in chunks:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-r1:free",
                messages=[
                    {
                        "role": "user",
                        "content": f"""Summarize the following content while preserving key details and maintaining clarity:\n\n
                        {chunk}\n\n
                        ### Summarization Guidelines:
                        1. **Concise & Informative:** Provide a well-structured summary that retains the most important points.
                        2. **No Extra Commentary:** Do not include opinions, interpretations, or unnecessary details.
                        3. **Maintain Original Meaning:** Ensure that the summary accurately reflects the original content without distortion.
                        4. **Readable & Coherent:** The output should be easy to understand, structured, and free from redundancy.
                        """
                    }
                ]
            )
            summarized_data.append(completion.choices[0].message.content)
            
        final_summary = "\n\n".join(summarized_data)  # spacing for readability

        return final_summary
    
    def get_title(self,summary):

        client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key="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"
            )
        
        # Generate title based on the final summary
        title_completion = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "user",
                    "content": f"""Generate a concise and engaging title based on the following summary:\n\n
                    {summary}\n\n
                    ### Title Guidelines:
                    1. **Short & Catchy:** Keep the title concise and attention-grabbing.
                    2. **Reflect the Summary:** Ensure the title accurately represents the main idea.
                    3. **Avoid Clickbait:** The title should be informative.
                    4. **Max 8 Words:** Keep the title brief and impactful.
                    """
                }
            ]
        )

        title = title_completion.choices[0].message.content.strip()  # Extract title and remove extra spaces
        title = title.split("\n")[0].strip()  #getting 1st line from response
        
        # Remove "**Title:**" or "*Title:*" if present
        clean_title = re.sub(r"^\**Title:\**\s*", "", title)

        # Remove any leading/trailing asterisks
        clean_title = clean_title.strip("*")

        return title
