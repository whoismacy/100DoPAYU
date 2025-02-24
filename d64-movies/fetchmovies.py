import requests
import time
import os
from dotenv import load_dotenv
import renderdb

load_dotenv()

API_ENDPOINT = "http://www.omdbapi.com/"
API_KEY = os.getenv("API_KEY")
EXISTING_MOVIES = renderdb.all_movie_titles()

class FetchMovies:
    def __init__(self):
        self.movie_list = []

    def fetch_movie(self, *args):
        for arg in args:
            if arg.title() not in EXISTING_MOVIES:
                parameter = {
                    "apikey": API_KEY,
                    "t": arg,
                    "type": "movie",
                    "plot": "short",
                    "r": "json",
                }

                try:
                    response = requests.get(url=API_ENDPOINT, params=parameter)
                    response.raise_for_status()
                    data = response.json()

                    if data['Response'] == "False":
                        raise Exception("Unknown API Error !!!")
                    else:
                        title = data.get("Title", "Unknown")
                        year = data.get("Year", "Unknown")
                        plot = data.get("Plot", "N/A").replace('\\', '')
                        poster_link = data.get("Poster", "No Poster Found")
                        rating = data.get("Ratings", [])
                        rotten_tomato_rating = "N/A"

                        for rate in rating:
                            if rate['Source'] == "Rotten Tomatoes":
                                rotten_tomato_rating = rate['Value']
                                break

                        movie_dict = {
                            'title': title,
                            'year': int(year) if year.isdigit() else None,
                            'plot': plot,
                            'poster_link': poster_link,
                            'rt_rating': rotten_tomato_rating,
                        }
                        self.movie_list.append(movie_dict)
                    time.sleep(1)
                except Exception as e:
                    print(f"Failed to fetch Movies: {e}")

    def remove_movie(self, movie_name):
        movie_name = movie_name.title()
        for film in self.movie_list:
            if film['title'] == movie_name:
                self.movie_list.remove(film)
                return True
        return False

    def get_as_list(self):
        return self.movie_list


# movies = ("Cars 2", "Finding Nemo", "despicable me 3")
# movie_fetcher = FetchMovies()
# movie_fetcher.fetch_movie(*movies)
# print(movie_fetcher.get_as_list())
# movie_fetcher.remove_movie("Finding Nemo")
# print(movie_fetcher.get_as_list())
# movies = ("There will be blood", "12 Years a Slave", "Inglourious Basterds", "In the mood for love", "La Haine", "Sound of Metal", "No country for old men", "birdman", "parasite", "Memories of murder", "incendies")
# get_movie = FetchMovies()
# get_movie.fetch_movie(*movies)
# print(get_movie.get_as_list())
# # print(API_KEY)