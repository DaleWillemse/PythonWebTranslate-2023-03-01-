from bs4 import BeautifulSoup

with open("www_classcentral_default.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")


paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.get_text())
