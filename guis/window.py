from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication, QDialog,
    QGridLayout, QSizePolicy)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *

class Window(QDialog):
    def __init__(self, parent = None):
        """ Initialisiere das Fenster """

        super().__init__(parent)
        self.Labels = {}
        self.Buttons = {}
        self.Edits = {}
        self.Layouts = {}
        self.Icons = {}

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
        self.BorderLine2 = QLabel("<hr>")

        # Definiere Icons
        self.Icons["cancel"] = QIcon("res/img/cancel.png")
        self.Icons["left"] = QIcon("res/img/left.png")
        self.Icons["right"] = QIcon("res/img/right.png")

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

        # Füge Navigationsleiste hinzu
        self.Layouts["hboxnavbar"] = QHBoxLayout()

        self.Layouts["vboxnavbar"] = QVBoxLayout()
        self.Layouts["vboxnavbar"].addWidget(self.BorderLine2)
        self.Layouts["vboxnavbar"].addLayout(self.Layouts["hboxnavbar"])

        # Initialisiere vertikales Layout
        self.Layouts["vbox"] = QVBoxLayout()
        self.Layouts["vbox"].addLayout(self.Layouts["vboxtitlebar"])
        # self.Layouts["vbox"].addStretch()

        # Setze Layout für das Fenster
        self.setLayout(self.Layouts["vbox"])

    def cancel (self):
        pass

    def add_cancel_button (self, text = "Abbrechen"):
        self.Buttons["cancel"] = QPushButton(text)
        self.Buttons["cancel"].setIcon(self.Icons["cancel"])
        self.Buttons["cancel"].setFixedHeight(70)
        self.Buttons["cancel"].clicked.connect(self.cancel)
        self.Layouts["hboxnavbar"].addWidget(self.Buttons["cancel"])

    def back (self):
        pass

    def add_back_button (self, text = "Zurück"):
        self.Buttons["back"] = QPushButton(text)
        self.Buttons["back"].setIcon(self.Icons["left"])
        self.Buttons["back"].setFixedHeight(70)
        self.Buttons["back"].clicked.connect(self.back)
        self.Layouts["hboxnavbar"].addWidget(self.Buttons["back"])

    def next (self):
        pass

    def add_next_button(self, text = "Weiter"):
        self.Buttons["next"] = QPushButton(text)
        self.Buttons["next"].setIcon(self.Icons["right"])
        self.Buttons["next"].setFixedHeight(70)
        self.Buttons["next"].clicked.connect(self.next)
        self.Layouts["hboxnavbar"].addWidget(self.Buttons["next"])

    def finish_ui (self):
        #self.Layouts["vbox"].addStretch()
        self.Layouts["vbox"].addLayout(self.Layouts["vboxnavbar"])
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
        self.updated_must_check()

    def updated_must_check (self):
        pass
