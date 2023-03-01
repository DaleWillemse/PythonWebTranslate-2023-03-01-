import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import time

# Set the starting URL and the maximum number of pages to download
start_url = "https://www.classcentral.com"
max_depth = 2

# Define a function to download a single page and all the pages linked to it


def download_page(url, depth=0):
    # Fetch the HTML content of the page
    response = requests.get(url)

    # Wait for one second before proceeding
    time.sleep(1)

    html = response.content

    # Parse the HTML and extract the links to other pages
    soup = BeautifulSoup(html, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]

    # Download each linked page recursively
    for link in links:
        # Skip links that are not valid URLs
        if not link:
            continue

        # Convert relative URLs to absolute URLs
        link_url = urljoin(url, link)

        # Skip links to other domains
        if urlparse(link_url).netloc != urlparse(url).netloc:
            continue

        # Download the linked page if it hasn't been downloaded already
        if link_url not in visited_urls and depth < max_depth:
            visited_urls.add(link_url)
            download_page(link_url, depth+1)

    # Save the HTML content of the page to a file
    with open(urlparse(url).netloc + urlparse(url).path + ".html", "wb") as f:
        f.write(html)


# Download the starting page and all the pages linked to it
visited_urls = set([start_url])
download_page(start_url)
