import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy import SpotifyOAuth

load_dotenv()
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
user = os.getenv("spotify_user")
REDIRECT_URL = "http://example.com"

header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
}

url = "https://www.billboard.com/charts/hot-100/"
date = input("Which year do you want to travel to ? type YYYY-MM-DD: ").strip()

response = requests.get(url=f"{url}{date}", headers=header)

soup = BeautifulSoup(response.text, 'html.parser')
song_name_span = soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_name_span]

display_name = ''
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URL,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username=user))

playlist = sp.user_playlist_create(name=f"{date} Billboard 100", user=user, public=False)
playlist_id = playlist['id']
tracks_uris = []

for i in song_names:
    results = sp.search(q=i)
    if results:
        tracks_uris.append(results['tracks']['items'][0]['uri'])

sp.user_playlist_add_tracks(user=user, playlist_id=playlist_id, tracks=tracks_uris)
