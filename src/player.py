from composition import Composition
from playlist import PlayList
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QListWidget,
    QHBoxLayout, QLabel, QInputDialog, QFileDialog,
    QComboBox, QListWidgetItem, QMessageBox
)
from pygame import mixer, USEREVENT
import pygame
import os


class MusicPlayer(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.playlists = {}
        self.current_playlist = None
        self.current_playlist_name = None
        self.track_end_event = USEREVENT + 1
        self.is_paused = False

        pygame.init()
        mixer.init()
        mixer.music.set_endevent(self.track_end_event)

        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_track_end_event)
        self.timer.start(100)

    def init_ui(self) -> None:
        """Создание интерфейса"""
        main_layout = QVBoxLayout()
        controls_layout = QHBoxLayout()

        self.playlist_combo = QComboBox()
        self.playlist_combo.currentIndexChanged.connect(self.switch_playlist)

        self.add_playlist_btn = QPushButton("Добавить плейлист")
        self.delete_playlist_btn = QPushButton("Удалить плейлист")
        self.add_playlist_btn.clicked.connect(self.create_playlist)
        self.delete_playlist_btn.clicked.connect(self.delete_playlist)

        self.play_btn = QPushButton("Воспроизвести")
        self.pause_btn = QPushButton("Пауза")
        self.next_btn = QPushButton("Следующий")
        self.prev_btn = QPushButton("Предыдущий")
        self.add_track_btn = QPushButton("Добавить трек")
        self.delete_track_btn = QPushButton("Удалить трек")

        self.move_up_btn = QPushButton("Передвинуть вверх")
        self.move_down_btn = QPushButton("Передвинуть вниз")

        self.play_btn.clicked.connect(self.play_track)
        self.pause_btn.clicked.connect(self.pause_track)
        self.next_btn.clicked.connect(self.next_track)
        self.prev_btn.clicked.connect(self.prev_track)
        self.add_track_btn.clicked.connect(self.add_track)
        self.delete_track_btn.clicked.connect(self.delete_track)

        self.move_up_btn.clicked.connect(self.move_track_up)
        self.move_down_btn.clicked.connect(self.move_track_down)

        self.track_list = QListWidget()
        self.track_list.itemDoubleClicked.connect(self.double_click_play)

        self.current_track_label = QLabel("Текущий трек: Нет трека")

        controls_layout.addWidget(self.add_playlist_btn)
        controls_layout.addWidget(self.delete_playlist_btn)
        controls_layout.addWidget(self.play_btn)
        controls_layout.addWidget(self.pause_btn)
        controls_layout.addWidget(self.next_btn)
        controls_layout.addWidget(self.prev_btn)
        controls_layout.addWidget(self.add_track_btn)
        controls_layout.addWidget(self.delete_track_btn)

        controls_layout.addWidget(self.move_up_btn)
        controls_layout.addWidget(self.move_down_btn)

        main_layout.addWidget(self.playlist_combo)
        main_layout.addWidget(self.track_list)
        main_layout.addWidget(self.current_track_label)
        main_layout.addLayout(controls_layout)

        self.setLayout(main_layout)

        self.setWindowTitle("Музыкальный плеер")
        self.setGeometry(300, 300, 600, 400)

    def update_current_track_label(self) -> None:
        """Обновление текущего трека"""
        if self.current_playlist and self.current_playlist.current:
            self.current_track_label.setText(f"Текущий трек: {self.current_playlist.current.title}")
        else:
            self.current_track_label.setText("Текущий трек: Нет трека")

    def create_playlist(self) -> None:
        """Создание плейлиста"""
        name, ok = QInputDialog.getText(self, 'Новый плейлист', 'Введите название плейлиста:')
        if ok and name:
            self.playlists[name] = PlayList()
            self.playlist_combo.addItem(name)
            self.playlist_combo.setCurrentText(name)

    def delete_playlist(self) -> None:
        """Удалить текущий плейлист"""
        if self.current_playlist_name:
            self.track_list.clear()
            del self.playlists[self.current_playlist_name]
            index_to_remove = self.playlist_combo.currentIndex()
            self.playlist_combo.blockSignals(True)
            self.playlist_combo.removeItem(index_to_remove)
            self.playlist_combo.blockSignals(False)

            if self.playlist_combo.count() > 0:
                self.playlist_combo.setCurrentIndex(0)
                self.switch_playlist()
            else:
                self.current_playlist = None
                self.current_playlist_name = None
                self.track_list.clear()
                self.update_current_track_label()

    def switch_playlist(self) -> None:
        """Смена плейлиста"""
        self.current_playlist_name = self.playlist_combo.currentText()
        if self.current_playlist_name:
            self.current_playlist = self.playlists[self.current_playlist_name]
            self.update_track_list()
            self.update_current_track_label()

    def add_track(self) -> None:
        """Добавить трек в текущий плейлист"""
        if not self.playlists:
            QMessageBox.warning(self, "Плейлист отсутствует", "Создайте плейлист перед добавлением трека.")
            return

        file_dialog = QFileDialog()
        track_path, _ = file_dialog.getOpenFileName(self, "Добавить трек", "", "MP3 Files (*.mp3)")
        if track_path:
            track_name = os.path.basename(track_path)
            composition = Composition(track_name, track_path)
            self.current_playlist.append(composition)
            self.update_track_list()

    def delete_track(self) -> None:
        """Удалить трек из плейлиста"""
        selected_item = self.track_list.currentItem()
        if selected_item and self.current_playlist:
            track_name = selected_item.text()
            track_to_delete = None
            for track in self.current_playlist:
                if track.data.title == track_name:
                    track_to_delete = track.data
                    break
            if track_to_delete:
                self.current_playlist.remove(track_to_delete)
                self.update_track_list()
                self.update_current_track_label()

    def update_track_list(self) -> None:
        """Обновление плейлиста"""
        self.track_list.clear()
        if self.current_playlist:
            for track in self.current_playlist:
                item = QListWidgetItem(str(track.data))
                item.setData(Qt.UserRole, track.data.path)
                self.track_list.addItem(item)

    def play_track(self) -> None:
        """Воспроизвести текущий выбранный трек"""
        if not self.current_playlist or len(self.current_playlist) == 0:
            QMessageBox.warning(self, "Трек отсутствует", "Плейлист пуст. Добавьте трек.")
            return

        if self.is_paused:
            mixer.music.unpause()
            self.is_paused = False
        else:
            selected_item = self.track_list.currentItem()
            if selected_item and self.current_playlist:
                track_name = selected_item.text()
                for track in self.current_playlist:
                    if track.data.title == track_name:
                        self.current_playlist.play_track(track.data)
                        self.is_paused = False
                        self.update_current_track_label()
                        break

        pygame.event.clear(self.track_end_event)

    def double_click_play(self, item) -> None:
        """Воспроизведение по двойному нажатию"""
        if item:
            track = Composition(item.text(), item.data(Qt.UserRole))
            for node in self.current_playlist:
                if node.data.title == track.title:
                    self.current_playlist.current_track = node
                    break
            self.current_playlist.play_track(track)
            self.is_paused = False
            self.update_current_track_label()
            pygame.event.clear(self.track_end_event)
            mixer.music.set_endevent(self.track_end_event)

    def next_track(self) -> None:
        """Перейти к следующему треку и воспроизвести его"""
        if not self.current_playlist or len(self.current_playlist) == 0:
            QMessageBox.warning(self, "Трек отсутствует", "Плейлист пуст. Добавьте трек.")
            return
        if self.current_playlist:
            self.current_playlist.next_track()
        self.is_paused = False
        self.update_current_track_label()

    def prev_track(self) -> None:
        """Воспроизвести предыдущий трек, если плейлист не пуст"""
        if not self.current_playlist or len(self.current_playlist) == 0:
            QMessageBox.warning(self, "Трек отсутствует", "Плейлист пуст. Добавьте трек.")
            return
        if self.current_playlist:
            self.current_playlist.previous_track()
        self.is_paused = False
        self.update_current_track_label()

    def move_track_up(self) -> None:
        """Передвинуть трек вверх"""
        selected_row = self.track_list.currentRow()
        if selected_row != -1 and selected_row > 0:
            item = self.track_list.takeItem(selected_row)
            self.track_list.insertItem(selected_row - 1, item)
            self.track_list.setCurrentRow(selected_row - 1)

            self.current_playlist.move_item_up(selected_row)
            self.update_current_track_label()

    def move_track_down(self) -> None:
        """Передвинуть трек вниз"""
        selected_row = self.track_list.currentRow()
        if selected_row != -1 and selected_row < self.track_list.count() - 1:
            item = self.track_list.takeItem(selected_row)
            self.track_list.insertItem(selected_row + 1, item)
            self.track_list.setCurrentRow(selected_row + 1)

            self.current_playlist.move_item_down(selected_row)
            self.update_current_track_label()

    def pause_track(self) -> None:
        """Пауза"""
        mixer.music.pause()
        self.is_paused = True

    def check_track_end_event(self) -> None:
        for event in pygame.event.get():
            if event.type == self.track_end_event:
                self.next_track()
