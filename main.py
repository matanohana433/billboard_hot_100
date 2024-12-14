import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
print("Please wait...")
header = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

URL = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=URL, headers=header)
bill_web_page = response.text

soup = BeautifulSoup(bill_web_page, 'html.parser')


top_songs_tag = soup.select('li ul li h3')

top_songs_list = [tag.getText().strip() for tag in top_songs_tag]





SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")

SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
APP_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=APP_REDIRECT_URI,
                                               scope="playlist-modify-private"))



my_username = sp.current_user()['id']
playlist_name = f"Billboard Hot 100 from {date}"

uri_list = []
year = date.split("-")[0]

for song in top_songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri_list.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesnt exists in spotify")

# print(uri_list)

playlist = sp.user_playlist_create(user=my_username, name=playlist_name, public=False)

playlist_id = playlist['id']

sp.playlist_add_items(playlist_id=playlist_id, items=uri_list)

print(f"Here is your link: {playlist['external_urls']['spotify']}, Enjoy :)")
