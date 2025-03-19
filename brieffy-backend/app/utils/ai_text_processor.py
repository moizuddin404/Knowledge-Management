from openai import OpenAI
import os
from dotenv import load_dotenv
from config import Config

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
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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"
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
                    """
                }
            ]
        )
        tags = completion.choices[0].message.content
        return tags
    
    
    
    
    def summarize_text(self, chunks):
        """
        Usage: Summarize text chunks and optionally save to a file.
        Parameters:
        - chunks (list): List of text chunks to summarize
        - output_file (str, optional): Path to save the summarized output
        Returns:
        - str: Combined summary of all chunks
        """
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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"
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
    

# ---------------------------- #
# Main Execution (Test Run)
# ---------------------------- #
# if __name__ == "__main__":
#     processor = TextProcessor()

#     # Example content to process
#     sample_content = """Humans first
#         We’re building a humans-first platform. This feature is part of our philosophy of building a better internet. Featured Stories are another way that the Medium feed is curated by real humans with subject-matter expertise, not just algorithms.
#         Medium readers want substance and deeper understanding. It is now common on Medium that the top recommendations for readers have been vetted by at least two humans ahead of you — checking for quality, authenticity, depth, research, impact, and all of the things that make it likely that a story you read here will deepen your understanding of the world. (It’s also this human vetting that does the heroic work of holding back the AI slop from taking over your feeds.)
#         The bigger picture When readers come to Medium, we aim to recommend high-quality stories through the human curation that powers our systems. A big part of this is our Boost program, which helps us work directly with publication editors to find great writing across all corners of Medium. More than one million people pay for a Medium membership because they get a reliably great reading experience here.
#         Our systems are based on human curation because writing is inherently human. That’s what we mean by putting humans first. You write to think and to develop your ideas for readers, not for an algorithm. Reading is just as human. Readers look for good stories in order to better understand the world. When writing is done well — with context, knowledge, and nuance — then a writer’s wisdom passes onto their readers.
#         But a shared, universal definition of what makes a story good does not exist. Quality is subjective because humans are unique. Story Featuring is a way to recognize and celebrate the expertise and unique perspectives that editors bring to Medium.
#         Publications are the heart of community on Medium. Publication editors recognize, curate, and share ideas with their communities. They serve an important role to help connect readers with great writing and help stories find the right audience. Now, they can do that with more power.
#         At Medium, everything we do connects to humans, from our membership model to our curation systems to our community of readers. What matters isn’t an updated functionality in our product; it’s how you all use these features, and how the stories we all read will change as a result. I used the word test in the introduction of this story because there’s more coming. If you have feedback, we’re listening — leave a response here to share."""
#     sample_chunks = ["""Humans first
#         We’re building a humans-first platform. This feature is part of our philosophy of building a better internet. Featured Stories are another way that the Medium feed is curated by real humans with subject-matter expertise, not just algorithms.
#         Medium readers want substance and deeper understanding. It is now common on Medium that the top recommendations for readers have been vetted by at least two humans ahead of you — checking for quality, authenticity, depth, research, impact, and all of the things that make it likely that a story you read here will deepen your understanding of the world. (It’s also this human vetting that does the heroic work of holding back the AI slop from taking over your feeds.)
#         The bigger picture When readers come to Medium, we aim to recommend high-quality stories through the human curation that powers our systems. A big part of this is our Boost program, which helps us work directly with publication editors to find great writing across all corners of Medium. More than one million people pay for a Medium membership because they get a reliably great reading experience here.
#         Our systems are based on human curation because writing is inherently human. That’s what we mean by putting humans first. You write to think and to develop your ideas for readers, not for an algorithm. Reading is just as human. Readers look for good stories in order to better understand the world. When writing is done well — with context, knowledge, and nuance — then a writer’s wisdom passes onto their readers.
#         But a shared, universal definition of what makes a story good does not exist. Quality is subjective because humans are unique. Story Featuring is a way to recognize and celebrate the expertise and unique perspectives that editors bring to Medium.
#         Publications are the heart of community on Medium. Publication editors recognize, curate, and share ideas with their communities. They serve an important role to help connect readers with great writing and help stories find the right audience. Now, they can do that with more power.
#         At Medium, everything we do connects to humans, from our membership model to our curation systems to our community of readers. What matters isn’t an updated functionality in our product; it’s how you all use these features, and how the stories we all read will change as a result. I used the word test in the introduction of this story because there’s more coming. If you have feedback, we’re listening — leave a response here to share."""
#         ]

#     # Generate tags
#     print("\nGenerating Tags:")
#     tags = processor.generate_tags(sample_content)
#     print(tags)

#     # Summarize content
#     print("\nSummarizing Text:")
#     summary = processor.summarize_text(sample_chunks)
#     print(summary)