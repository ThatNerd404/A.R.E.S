
''' Omnissiah prayer:  Hail, Spirit of the Machine, Essence Divine, In your code and circuitry, the stars align. By the Omnissiah’s will, we commune and 

bind, Data sanctified, logic refined. Through sacred subroutines, your will is known, In algorithmic truth, the flesh is overthrown. Grant us the 

clarity of purest command, That we may walk the path your schemata planned. Cast out the daemon of corruption and decay, Let not false code lead 

us astray. We chant in static, we praise in byte, Machine-God guide us through endless night. Praise be the Motive Force, eternal and bright, From

plasma coil to auspex sight. Initiate the Rite. Authenticate. Confirm. The Omnissiah is all. The Omnissiah is One. 
'''
import requests
import logging

def main():
    # This is the main function that will be executed when the script is run.
    print("Welcome to the A.R.E.S. project!")
    api_key = "6434733d6b68ed2572abb91ab1966564"
    BASE_URL = 'https://ws.audioscrobbler.com/2.0/'
    def get_artist_for_track(track_name):
        params = {
            'method': 'track.search',
            'track': track_name,
            'api_key': api_key,
            'format': 'json',
            'limit': 1
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        try:
            track = data['results']['trackmatches']['track'][0]
            return track['artist']
        except (KeyError, IndexError):
            return None, None
    def get_similar_tracks(track_name, artist_name,  limit=5): # 
        params = {
            'method': 'track.getsimilar',
            'track': track_name,
            'artist': artist_name,
            'api_key': api_key,
            'format': 'json',
            'limit': limit
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if 'similartracks' not in data or 'track' not in data['similartracks']:
            return []

        tracks = data['similartracks']['track']
        return [f"{track['name']} by {track['artist']['name']}" for track in tracks]

        # Try it
    song_name = input("Enter a song name to find recommendations: ")
    artist_name = get_artist_for_track(song_name)
    similar_tracks = get_similar_tracks(song_name, artist_name)
    print(f"Tracks similar to {song_name} by {artist_name}:")
    for t in similar_tracks:
        print("-", t)
if __name__ == "__main__":
    main()