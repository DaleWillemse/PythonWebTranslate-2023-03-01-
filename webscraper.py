from bs4 import BeautifulSoup
import requests

url = 'https://www.classcentral.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.0'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')

# print each link's URL
for link in links:
    href = link.get('href')
    if href.startswith('http'):
        print(href)
    else:
        print(url + href)
