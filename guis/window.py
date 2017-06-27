from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication,
    QGridLayout)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self):
        """ Initialisiere das Fenster """

        super().__init__()
        self.Labels = {}
        self.Buttons = {}
        self.Edits = {}
        self.Layouts = {}

        # Importiere die Einstellungen
        from settings import Settings
        self.Settings = Settings("config.json")

        # Initialisiere die UI und den Mainloop
        self.init_window_ui()
        self.init_must_check()

    def init_window_ui (self):
        # Zeige das Fenster im Vollbild
        self.showFullScreen()

        # Definiere eine vorgefertigte Linie
        self.BorderLine = QLabel("<hr>")

        # Definiere Labels für Titelleiste
        self.Labels["title"] = QLabel("<h1>" + self.Settings.get("company_name") + "</h1>")
        self.Labels["title"].setAlignment(Qt.AlignLeft)
        self.Labels["time"] = QLabel("")
        self.Labels["time"].setAlignment(Qt.AlignRight)
        self.update_time(self.Labels["time"])

        # Füge die Titelleiste hinzu
        self.Layouts["hboxtitlebar"] = QHBoxLayout()
        self.Layouts["hboxtitlebar"].addWidget(self.Labels["title"])
        self.Layouts["hboxtitlebar"].addWidget(self.Labels["time"])

        self.Layouts["vboxtitlebar"] = QVBoxLayout()
        self.Layouts["vboxtitlebar"].addLayout(self.Layouts["hboxtitlebar"])
        self.Layouts["vboxtitlebar"].addWidget(self.BorderLine)

        # Initialisiere vertikales Layout
        self.Layouts["vbox"] = QVBoxLayout()
        self.Layouts["vbox"].addLayout(self.Layouts["vboxtitlebar"])
        # self.Layouts["vbox"].addStretch()

        # Setze Layout für das Fenster
        self.setLayout(self.Layouts["vbox"])

    def finish_ui (self):
        self.Layouts["vbox"].addStretch()
        self.show()

    def update_time (self, time_label):
        """ Aktualisiert die Zeit in einem Label """
        import helper
        time = helper.get_time()
        time_label.setText("<h1>" + time + "</h1>")

    def init_must_check (self):
        """ Initialisert einen "Mainloop" """
        self.WindowMustCheckTimer = QTimer()
        self.WindowMustCheckTimer.timeout.connect(self.must_check)
        self.WindowMustCheckTimer.start(100)

    def must_check (self):
        """ Führt den Mainloop durch """
        self.update_time(self.Labels["time"])
        self.WindowMustCheckTimer.start(100)
