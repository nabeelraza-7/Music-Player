#! python3
# Music player app to play music.
########### alternative ##########
# import winsound

# filename = 'alarm.wav'
# winsound.PlaySound(filename, winsound.SND_FILENAME)


import os, sys
from playsound import playsound
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from layout import Ui_MainWindow

DOWNLOADS_FOLDER = os.path.expanduser("~") + "/Downloads/"
DIR = os.path.abspath('./' + __file__)

# testing playsound
# playsound('alarm.wav')
# print(DOWNLOADS_FOLDER)
class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.filename_lbl.setText("Music Player")
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionExit.triggered.connect(self.exit_player)
        self.ui.play_btn.clicked.connect(self.play_music)

        self.loaded_file = False
        self.location = ''

    def open_file(self):
        filenames = QFileDialog.getOpenFileName(self, 'Open File', DIR, "Audio files (*.wav *.mp3)")
        self.location = filenames[0]
        self.loaded_file = True

    def play_music(self):
        if self.loaded_file:
            self.ui.play_btn.setEnabled(False)
            playsound(self.location)
            self.ui.play_btn.setEnabled(True)

    def exit_player(self):
        sys.exit()

if __name__ == ("__main__"):
    app = QApplication([])
    w = Player()
    w.show()
    sys.exit(app.exec_())
