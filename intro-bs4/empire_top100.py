import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = BeautifulSoup(response.text, "html.parser")

all_h3s = content.find_all(name="h3", class_="title")
movies = [h3.get_text() for h3 in all_h3s]

with open("to_watch.txt", mode="w") as file:
    for i in range(len(movies))[::-1]:
        file.write(f"{movies[i]}\n")
