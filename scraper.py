from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

IMPORTANT_KEYWORDS = ["about", "company", "solution", "product", "customer", "contact"]

def extract_full_company_data(base_url):
    collected_text = ""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(base_url, timeout=60000)
        page.wait_for_timeout(5000)

        soup = BeautifulSoup(page.content(), "html.parser")

        # Collect homepage text
        collected_text += soup.get_text(separator="\n")

        # Find internal important links
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            full_url = urljoin(base_url, href)

            if urlparse(full_url).netloc == urlparse(base_url).netloc:
                if any(keyword in full_url.lower() for keyword in IMPORTANT_KEYWORDS):
                    links.append(full_url)

        # Visit important pages
        for link in list(set(links))[:5]:  # limit pages
            try:
                page.goto(link, timeout=60000)
                page.wait_for_timeout(4000)
                sub_soup = BeautifulSoup(page.content(), "html.parser")
                collected_text += "\n" + sub_soup.get_text(separator="\n")
            except:
                pass

        browser.close()

    return collected_text[:20000]