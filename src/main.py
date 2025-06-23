import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
from collections import Counter

# variables
track_limit = 50    # the amount of tracks to scan
times_played = 3    # amount of times a track needs to be played to recommend


# AUTH HANDLING
load_dotenv()
_ClientID= os.getenv("SPOTIPY_CLIENT_ID")
_ClientSecret=os.getenv("SPOTIPY_CLIENT_SECRET")
_RedirectURI=os.getenv("RedirectURI")

scope = "user-read-recently-played"
auth_READ = SpotifyOAuth(scope=scope, client_id=_ClientID, client_secret=_ClientSecret, redirect_uri=_RedirectURI)
SP_READ = spotipy.Spotify(auth_manager=auth_READ)


# reading track history
tracks = SP_READ.current_user_recently_played(track_limit)['items']

recently_played = []

for track in tracks:
    track_name = track['track']['name'] + " - " + track['track']['album']['artists'][0]['name']
    recently_played.append(track_name)


# Recommendation
counter_items = Counter(recently_played).items()

track_recommendations = []

print(counter_items)

for track in counter_items:
    if(track[1] >= times_played):
        track_recommendations.append(track)
        
if(len(track_recommendations) == 0):
    print("No tracks to recommend")

