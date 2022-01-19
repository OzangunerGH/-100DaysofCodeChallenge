import requests
from datetime import date
import os
# This block of code gets the last 3 news articles related to the company defined at COMPANY_NAME variable.
# The content of the news articles are their headers and URLs to read the full article.


API_KEY = os.environ.get("NEWS_API_KEY")
COMPANY_NAME = "Tesla Inc."
DATE = str(date.today())
SORT_TYPE = "publishedAt"
parameters = {"q": COMPANY_NAME,
              "from": DATE,
              "sortBy": SORT_TYPE,
              "apiKey": API_KEY}

response = requests.get("https://newsapi.org/v2/everything", params=parameters)
response.raise_for_status()
data = response.json()["articles"]
message_text = ""
for i in range(3):
    message = data[i]["title"]
    url = data[i]["url"]
    message_text += f"{message},\n {url}\n"
