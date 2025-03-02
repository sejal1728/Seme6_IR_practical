import requests
from bs4 import BeautifulSoup

# Specify the URL you want to scrape
url = "https://google.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and print the text content (modify as needed based on the HTML structure)
    text_content = soup.get_text()

    print(text_content)
else:
    print(f"Error: Unable to fetch content. Status code: {response.status_code}")
