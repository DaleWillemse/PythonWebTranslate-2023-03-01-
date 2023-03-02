import requests
from bs4 import BeautifulSoup


def translate_text(text, source_language, target_language):
    # MyMemory API endpoint
    url = "https://api.mymemory.translated.net/get"

    # Make the API request
    response = requests.get(url, params={
        "q": text,
        "langpair": f"{source_language}|{target_language}"
    })

    # Parse the API response
    json_response = response.json()
    if "responseData" in json_response and "translatedText" in json_response["responseData"]:
        # Return the translated text if the API was able to translate the input text
        return json_response["responseData"]["translatedText"]
    else:
        # Return None if the API was unable to translate the input text
        return None


# Load the HTML file
with open("www_classcentral_default.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Define the tags to translate
tags_to_translate = ["h1", "h2", "h3", "h4", "h5", "h6", "span", "p"]

# Translate each tag's contents
for tag in soup.find_all(tags_to_translate):
    if tag.string:
        # Translate the tag's content to Hindi
        translated_text = translate_text(tag.string, "en", "hi")

        # Replace the tag's content with the translated text if the translation was successful
        if translated_text:
            tag.string.replace_with(translated_text)

# Write the translated HTML to a file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(str(soup))
