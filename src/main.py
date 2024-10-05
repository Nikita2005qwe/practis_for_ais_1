from PyQt5.QtWidgets import QApplication
from player import MusicPlayer
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
