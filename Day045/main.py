import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
result = response.text
soup = BeautifulSoup(result, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles = [title.getText() for title in titles]
titles.reverse()

with open("movies-list.txt", "a", encoding="utf8") as movies:
    for title in titles:
        movies.write(title +"\n")

