"""
Точка входа в программу
"""
import sys
from PyQt5.QtWidgets import QApplication
from player import MusicPlayer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
