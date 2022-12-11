import sys

from PySide6.QtWidgets import (
    QWidget, QApplication,
    QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog
)

from PySide6.QtCore import QUrl, Slot
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class MP3Player(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 300, 150
        self.setFixedSize(self.window_width, self.window_height)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.audio_output = QAudioOutput()
        self.media_player = QMediaPlayer()

        self.media_player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(50)

        open_button = QPushButton("Open")
        self.layout.addWidget(open_button)
        open_button.clicked.connect(self.choose_media)

        play_btn = QPushButton("Play")
        self.layout.addWidget(play_btn)
        play_btn.clicked.connect(self.play_audio)

        volume_control = QHBoxLayout()
        self.layout.addLayout(volume_control)

        audio_btn_up = QPushButton("+")
        audio_btn_down = QPushButton("-")

        audio_btn_up.clicked.connect(self.volume_up)
        audio_btn_down.clicked.connect(self.volume_down)

        volume_control.addWidget(audio_btn_up)
        volume_control.addWidget(audio_btn_down)

    @Slot()
    def choose_media(self):
        url, _ = QFileDialog.getOpenFileUrl(self, "Choose media",
                                       "",
                                       "Audio (*.mp3)")

        self.media_player.setSource(url)

    @Slot()
    def play_audio(self):
        if self.media_player.playbackState() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()

    @Slot()
    def volume_up(self):
        current_volume = self.audio_output.volume()
        self.audio_output.setVolume(current_volume + 0.05)

    @Slot()
    def volume_down(self):
        current_volume = self.audio_output.volume()
        self.audio_output.setVolume(current_volume - 0.05)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = MP3Player()
    player.show()

    sys.exit(app.exec())
