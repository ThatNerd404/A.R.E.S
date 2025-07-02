from PySide6.QtGui import QMovie, QKeyEvent, QFontDatabase, QKeySequence, QShortcut, QTextCursor
from PySide6.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from PySide6.QtCore import Qt, QPoint, QSettings, QEventLoop
from logging.handlers import RotatingFileHandler
from ARES_GUI import Ui_MainWindow
import logging
import requests
import os


class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("A.R.E.S. - Artist Recommendation and Exploration System")
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(os.path.join(
            'Logs', 'log.log'), maxBytes=100000, backupCount=5, encoding="utf-8")
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        self.api_key = "6434733d6b68ed2572abb91ab1966564"
        self.BASE_URL = 'https://ws.audioscrobbler.com/2.0/'
        
        self.logger.info("Initialization complete.")
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
        except (KeyError, IndexError):
            return None, None
        
    def get_similar_tracks(self,track_name, artist_name,  limit=5): # 
        params = {
            'method': 'track.getsimilar',
            'track': track_name,
            'artist': artist_name,
            'api_key': self.api_key,
            'format': 'json',
            'limit': limit
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if 'similartracks' not in data or 'track' not in data['similartracks']:
            return []

        tracks = data['similartracks']['track']
        return [f"{track['name']} by {track['artist']['name']}" for track in tracks]

        # Try it
    '''song_name = input("Enter a song name to find recommendations: ")
    artist_name = get_artist_from_track(song_name)
    similar_tracks = get_similar_tracks(song_name, artist_name)
    print(f"Tracks similar to {song_name} by {artist_name}:")
    for t in similar_tracks:
        print("-", t)'''