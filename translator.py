from bs4 import BeautifulSoup
import translators.server as tss

with open("www_classcentral_default.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

tags = ["h1", "h2", "h3", "h4", "h5", "h6",
        "p", "title", "span", "a", "div",
        "section", "strong"]

html_content = soup.find_all(tags)
for content in html_content:
    if content.string and not content.string.isspace():
        translation = tss.google(content.string, to_language='hi')
        content.string.replace_with(translation)

with open("TranslatedPage.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
