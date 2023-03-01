import requests

url = 'https://www.classcentral.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
response = requests.get(url, headers=headers)

with open('example.html', 'w') as f:
    f.write(response.text)
