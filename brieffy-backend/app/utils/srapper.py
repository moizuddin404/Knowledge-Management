from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

AUTH = 'brd-customer-hl_b5e721dc-zone-scraping_raw:iehizdgxsda8'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


class Scraper:
    def __init__(self, website):
            self.website = website

    def scrape_web(self):
        sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
        with Remote(sbr_connection, options=ChromeOptions()) as driver:
            print('Connected! Navigating...')
            driver.get(self.website)
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
        soup = BeautifulSoup(html, 'html.parser')
        body_content = soup.body
        if body_content:
            return str(body_content)
        else:
            return "No body content found"
        
    def clean_body_content(self,body_content):
        soup = BeautifulSoup(body_content, 'html.parser')

        # Remove unnecessary elements
        for tag in soup(['iframe', 'img', 'pre', 'script', 'style', 'hr', 'option', 'select', 'svg', 'video', 'input', 'nav', 'button', 'header', 'footer']):
            tag.extract()

        cleaned_text = soup.get_text(separator="\n")
        cleaned_text = "\n".join(line.strip() for line in cleaned_text.splitlines() if line.strip())
        return cleaned_text

    def split_content(self, web_content, max_length=6000):
        return [
            web_content[i:i+max_length] for i in range(0, len(web_content), max_length)
        ]
