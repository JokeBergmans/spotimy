import os
import json
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError

### run this in a terminal(use your own credentials)
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIFY_USERNAME='your-spotify-username-id' # usually a long string of alphanumeric characters
### youtube-dl is required, to install it, run this in a terminal
# sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
# sudo chmod a+rx /usr/local/bin/youtube-dl

### Vars
spotify=''
old_data=''
new_data=''


### Helper functions
def print_json(json_var):
    print(json.dumps(json_var, sort_keys=True, indent=4))

### General functions
def authenticate():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
    return null

def readData():
    playlists = sp.user_playlists(SPOTIFY_USERNAME)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == SPOTIFY_USERNAME:
            results = sp.user_playlist(SPOTIFY_USERNAME, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            # add to json to new_data
            
            while tracks['next']:
                tracks = sp.next(tracks)
                # add to json to new_data

    return null

def diffData():
    return null

def dataChanged():
    return null

def getNewSongs():
    return null

def downloadNewSongs():
    return null

def getRemovedSongs():
    return null

def removeOldSongs():
    return null

def saveNewData():
    return null




### Code structure
if authenticate():
    readData()
    diffData()
    if dataChanged():
        getNewSongs()
        downloadNewSongs()
        getRemovedSongs()
        removeOldSongs()
        saveNewData()
    else:
        print("no new songs")
else:
    print("could not authenticate")


        
