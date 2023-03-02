import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

url = 'addurlhere'
headers = {
    'add user agent here'
}

visited_urls = set()
urls_to_visit = set([url])

if not os.path.exists('html_pages'):
    os.makedirs('html_pages')


def save_html(url, content):
    path = os.path.join('html_pages', urlparse(
        url).path.lstrip('/').replace('/', '_') + '.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


while urls_to_visit:
    url = urls_to_visit.pop()
    visited_urls.add(url)
    print(f"Visiting {url}")

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
    except:
        continue

    # Save the HTML content to a file
    save_html(url, str(soup))

    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            print(href)
        elif href and not href.startswith('#'):
            link_url = url + href if href.startswith('/') else href
            parsed_url = urlparse(link_url)
            if parsed_url.netloc == urlparse(url).netloc and link_url not in visited_urls:
                urls_to_visit.add(link_url)
