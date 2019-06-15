import os
import json
import spotipy
import youtube_dl

from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError

# run this in a terminal(use your own credentials)
# export SPOTIPY_CLIENT_ID='your-spotify-client-id'
# export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
# export SPOTIFY_USERNAME='your-spotify-username-id' # usually a long string of alphanumeric characters

# Vars
# spotify = None
# old_data = []
# new_data = []
SPOTIFY_USERNAME = '21ivmo6qmkfa4dds7msub6tfy'
SPOTIPY_CLIENT_ID = '7546b18d1c22462faf611c49e6df7cbe'
SPOTIPY_CLIENT_SECRET = '4222e1fad6ab4afbb4fcef10fe9ce204'


# Helper functions
def print_json(json_var):
    print(json.dumps(json_var, sort_keys=True, indent=4))


def add_json_to_data(tracks, new_data):
    # TODO: implement
    for i, item in enumerate(tracks['items']):
        track = item['track']
        new_entry = "%s-%s" % (track['artists'][0]['name'], track['name'])
        new_data.append(new_entry)


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d    %-20s -  %s" % (i, track['artists'][0]['name'], track['name']))
        print("                  %s" % (track['album']['images'][0]['url']))


def sort_new_data(new_data):
    new_data.sort()


def download_new_song(track):
    # TODO: check for quotes and other special characters in track name and filter these out
    track = track.replace("\'", "").replace("/", " ").replace("\\", "")
    print("Downloading %s" % track)
    command = "youtube-dl -o \"music_downloads/%s" % track + ".%(ext)s\"" \
              + " --extract-audio --audio-format mp3 \"ytsearch1:%s\" > /dev/null" % track
    os.system(command)


def add_new_song(track, old_data):
    print("Adding \'%s\' to library" % track)
    old_data.append(track)


def remove_old_song(track, old_data):
    # TODO: also remove the song in music_downloads
    print("Removing old song from library")
    old_data.remove(track)
    return 0


def save_old_data(old_data):
    print("Saving data")
    with open("old_data.txt", "w") as outfile:
        for item in old_data:
            outfile.write("%s\n" % item)


# General functions
def main():
    print("Authenticating")
    # try:
    spotify = spotipy.Spotify(
        client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

    print("Reading old data")
    if os.path.isfile("old_data.txt"):
        print("File old_data.txt exists")
        with open("old_data.txt") as infile:
            old_data = infile.read().splitlines()
    else:
        print("File old_data.txt does not exists, creating empty file")
        with open("old_data.txt", "a"):
            os.utime("old_data.txt", None)
        old_data = []
    new_data = []

    print("Get and read new data")
    playlists = spotify.user_playlists(SPOTIFY_USERNAME)
    for playlist in playlists['items']:
        if playlist['owner']['id'] == SPOTIFY_USERNAME:
            results = spotify.user_playlist(SPOTIFY_USERNAME, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            add_json_to_data(tracks, new_data)

            while tracks['next']:
                tracks = spotify.next(tracks)
                add_json_to_data(tracks, new_data)

    sort_new_data(new_data)

    print("Diff-ing data")
    old_to_new = [x for x in old_data if x not in set(new_data)]
    new_to_old = [x for x in new_data if x not in set(old_data)]
    result = old_to_new + new_to_old

    # print(old_data)
    # print(new_data)

    # if there are differences, apply them, else do noting
    if len(result) > 0:
        print("Differences found")
        for item in result:
            if item in old_data and item not in new_data:
                # remove item from old_data
                remove_old_song(item, old_data)
            elif item not in old_data and item in new_data:
                # add item to old_data
                download_new_song(item)
                add_new_song(item, old_data)
            else:
                # idk
                print("Error")
        save_old_data(old_data)
    else:
        print("There are no differences")

    print("Success")
    # except:
    #     print("Error")


### Code structure
main()
