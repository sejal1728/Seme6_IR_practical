import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL of the website to crawl
base_url = "http://books.toscrape.com/"

# Set to store visited URLs
visited_urls = set()

# List to store URLs to visit next
urls_to_visit = [base_url]

# Function to crawl a page and extract links
def crawl_page(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=50)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract links and enqueue new URLs
        links = []
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])  # Convert relative URLs to absolute
            links.append(next_url)

        return links

    except requests.exceptions.RequestException as e:
        print(f"Error crawling {url}: {e}")
        return []

# Main loop to crawl pages
while urls_to_visit:
    current_url = urls_to_visit.pop(0)

    if current_url in visited_urls:
        continue

    print(f"Crawling: {current_url}")
    
    new_links = crawl_page(current_url)

    visited_urls.add(current_url)
    
    # Add new links to queue if they haven't been visited
    for link in new_links:
        if link not in visited_urls:
            urls_to_visit.append(link)
