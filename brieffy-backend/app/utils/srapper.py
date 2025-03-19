from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_b5e721dc-zone-scraping_raw:iehizdgxsda8'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

class Scraper:

    def scrape_web(self, website):
        """
        Usage: to scrape the website content using the selenium webdriver
        Parameters: website url
        Returns: html content of the website
        """
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            print('Connected! Navigating...')
            driver.get(website)
            # capta handling
            solve_res = driver.execute('executeCdpCommand', {
                'cmd' : 'Captcha.waitForSolve',
                'params' : {'detectTimeout' : 10000},
            })
            print('captcha solving status :', solve_res['value']['status'])
            print("navigated, scraping page content...")
            html = driver.page_source
            return html

    def extract_body_content(self,html):
        """
        Usage: to extract the body content from the html content
        Parameters: html content of the website
        Returns: body content of the website
        """
        soup = BeautifulSoup(html, 'html.parser')
        body_content = soup.body
        if body_content:
            return str(body_content)
        else:
            return "No body content found"
        
    def clean_body_content(self,body_content):
        """
        Usage: to clean the body content of the website
        Parameters: body content of the website"
        Returns: cleaned body content of the website
        """
        soup = BeautifulSoup(body_content, 'html.parser')

        # Remove unnecessary elements
        for tag in soup(['iframe', 'img', 'pre', 'script', 'style', 'hr', 'option', 'select', 'svg', 'video', 'input', 'nav', 'button', 'header', 'footer']):
            tag.extract()

        cleaned_text = soup.get_text(separator="\n")
        cleaned_text = "\n".join(line.strip() for line in cleaned_text.splitlines() if line.strip())
        return cleaned_text

    def split_content(self, web_content, max_length=6000):
        """
        Usage: to split the content into chunks to pass to the summarizer
        Parameters: web content, max length of each chunk
        Returns: list of content chunks
        """
        return [
            web_content[i:i+max_length] for i in range(0, len(web_content), max_length)
        ]


# test Run for the scraper
# if __name__ == "__main__":
    # test_url = "https://medium.com/@rjtavares/clustering-articles-using-llm-embeddings-the-easy-way-725ce58bb385"  # Change to the site you want to scrape
    # scraper = Scraper(test_url)

    # print("Scraping web page...")
    # html_content = scraper.scrape_web()

    # print("\nExtracting body content...")
    # body_content = scraper.extract_body_content(html_content)

    # print("\nCleaning content...")
    # cleaned_content = scraper.clean_body_content(body_content)

    # print("\nSplitting content into chunks...")
    # content_chunks = scraper.split_content(cleaned_content)

    # print("\nExtracted Content:")
    # for i, chunk in enumerate(content_chunks):
    #     print(f"\nChunk {i+1}:\n{chunk}")