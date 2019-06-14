import os
import json
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError

### run this in a terminal(use your own credentials)
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIFY_USERNAME='your-spotify-username-id' # usually a long string of alphanumeric characters

### Vars
spotify=''
old_data=[]
new_data=[]


### Helper functions
def print_json(json_var):
    print(json.dumps(json_var, sort_keys=True, indent=4))

def add_json_to_data(tracks):
    # TODO: implement
    for i, track in enumerate(tracks['items']):
        new_entry="%s-%s" % (track['name'], track['artists'][0]['name'])
        new_data.append(new_entry)

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
    track = item['track']
    print("   %d    %-20s -  %s" % (i, track['artists'][0]['name'], track['name']))
    # print("              %s" % (track['images']))
    print("                  %s" % (track['album']['images'][0]['url']))

def sort_new_data(new_data):
    new_data.sort()

### General functions
def readOldData(data):
    with open("old_data.txt") as infile:
        old_data = infile.read().splitlines()

def authenticate():
    try:
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
        return true
    except:
        return false

def readData():
    playlists = sp.user_playlists(SPOTIFY_USERNAME)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == SPOTIFY_USERNAME:
            results = sp.user_playlist(SPOTIFY_USERNAME, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            # TODO: add to json to new_data
            add_json_to_data(tracks)
            
            while tracks['next']:
                tracks = sp.next(tracks)
                # TODO: add to json to new_data
                add_json_to_data(tracks)

    sort_new_data(new_data)
    return null

def diffData(old_data, new_data):
    result = list(set(old_data) - set(new_data))
    # if there are differences, apply them, else do noting
    if len(result) > 0:
        for item in enumerate(result)
            if item in old_data and item not in new_data:
                # remove item from old_data
                removeOldSong(old_data)
            elif item not in old_data and item in new_data:
                # add item to old_data
                downloadNewSong()
                addNewSong(old_data)
            else:
                # idk
    else:
        print("there are no differences")


def downloadNewSong():
    return null

def removeOldSong():
    return null

def saveOldData(data):
    with open("old_data.txt", "w") as outfile:
        for item in data:
            outfile.write("%s\n" % item)


### Code structure
if authenticate():
    readData()
    diffData():
else:
    print("could not authenticate")


        
