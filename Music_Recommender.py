from PySide6.QtCore import QThread, Signal
import requests

class MusicRecommenderThread(QThread):
    finished = Signal(str,str,str)
    error = Signal(str)
    
    def __init__(self, liked_track, num_recommendations):
        super().__init__()
        self.liked_track = liked_track
        self.num_recommendations = num_recommendations
        self.api_key = "6434733d6b68ed2572abb91ab1966564"
        self.BASE_URL = 'https://ws.audioscrobbler.com/2.0/'

    def run(self):
        # Simulate recommendation logic
        try:
            # Get the artist from the liked track
            artist_name = self.get_artist_from_track(self.liked_track)
            if not artist_name:
                self.error.emit("Artist not found for the given track.")
                return
            
            # Get similar tracks
            similar_tracks = self.get_similar_tracks(self.liked_track, artist_name)
            if not similar_tracks:
                self.error.emit("No similar tracks found.")
                return
            
            # Emit the finished signal with the recommendations
            recommendations = "\n".join(similar_tracks)
            self.finished.emit(self.liked_track, artist_name, recommendations)
            
        except Exception as e:
            self.error.emit(str(e))
    
    def get_artist_from_track(self,track_name):
        params = {
            'method': 'track.search',
            'track': track_name,
            'api_key': self.api_key,
            'format': 'json',
            'limit': 1
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        
        try:
            track = data['results']['trackmatches']['track'][0]
            return track['artist']
        except:
            return None
    
    def get_similar_tracks(self,track_name, artist_name): # 
        params = {
            'method': 'track.getsimilar',
            'track': track_name,
            'artist': artist_name,
            'api_key': self.api_key,
            'format': 'json',
            'limit': self.num_recommendations
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if 'similartracks' not in data or 'track' not in data['similartracks']:
            return []

        tracks = data['similartracks']['track']
        return [f"{track['name']} by {track['artist']['name']}" for track in tracks]
