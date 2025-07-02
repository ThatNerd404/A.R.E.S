from PySide6.QtGui import QMovie, QKeyEvent, QFontDatabase, QKeySequence, QShortcut, QTextCursor
from PySide6.QtWidgets import QMainWindow, QInputDialog, QFileDialog
from PySide6.QtCore import Qt, QPoint, QSettings, QEventLoop
from PySide6 import QtWidgets
from logging.handlers import RotatingFileHandler
from ARES_GUI import Ui_MainWindow
from Music_Recommender import MusicRecommenderThread
from PySide6.QtCore import QThread, Signal
import logging
import os


class UserInterface(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("A.R.E.S. - Artist Recommendation and Exploration System")
        
        # iniitialize the logger
        if not os.path.exists('Logs'):
            os.makedirs('Logs')
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)
        handler = RotatingFileHandler(os.path.join(
            'Logs', 'log.log'), maxBytes=100000, backupCount=5, encoding="utf-8")
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',"%Y-%m-%d %H:%M:%S")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        self.testing_movie = QMovie(os.path.join('Assets', 'testing_gif.gif'))
        self.testing_gif.setMovie(self.testing_movie)
        self.testing_movie.start()
        self.Enter_button.clicked.connect(self.send_request)
        self.logger.info("Initialization complete.")
        
    def send_request(self):
        self.logger.info("Send request button clicked.")
        liked_track = self.User_input.text().strip()
        if not liked_track:
            self.logger.warning("No track entered.")
            return
        
        self.logger.info(f"User entered track: {liked_track}")
        self.recommender_thread = MusicRecommenderThread(liked_track)
        self.recommender_thread.finished.connect(self.display_recommendations)
        self.recommender_thread.error.connect(self.display_error)
        self.recommender_thread.start()
   
    def display_recommendations(self, liked_track, artist_name, recommendations):
        self.logger.info("Displaying recommendations.")
        self.Display.clear()
        self.Display.setText(f"Because you liked {liked_track} by {artist_name} you might like:\n{recommendations}")
        
        
    def display_error(self, error_message):
        self.logger.error(f"Error occurred: {error_message}")
        self.Display.clear()
        self.Display.setText(f"Error: {error_message}")
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UserInterface()
    window.show()
    sys.exit(app.exec())