#Importing necessary libraries.
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# Getting user to enter a date to get corresponding Billboard 100 list on that date.
date = input("What date would you like to travel to ? Enter in YYYY-MM-DD format.\n")

#Getting the year from the date to use it as a filter in spotify search for songs.
year = date.split("-")[0]

#Getting the Billboard 100 list by Webscraping using BeautifulSoup library Passing the song names of the Billboard 100 into a list named song_list.
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

result = response.text
soup = BeautifulSoup(result, 'html.parser')
song_name = soup.find_all("h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText() for song in song_name]

#Setting environment variables for Spotipy. Enter your own spotify client ID and Client secret as environment variables in order to make the code work.
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
scope = "playlist-modify-private"

# Authenticating to Spotipy.
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope,
                              redirect_uri="http://example.com",
                              client_id=client_id,
                              client_secret=client_secret,
                              show_dialog=True,
                              cache_path="token.txt")
)

# Getting user_id of the Spotipy.
user_id = sp.current_user()["id"]
song_uris = []
# Searching for the billboard 100 songs in Spotify, if they are found, passing the song uri's to a song_uris list.
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new spotify playlist, and adding the songs in song_uris to the newly created playlist.
playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False,
                                   description="Test playlist for python project.")

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris, position=None)
