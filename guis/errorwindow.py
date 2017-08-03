from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel, QListWidget,
    QMessageBox,
    QApplication, QDialog,
    QGridLayout, QSizePolicy, QTextEdit)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *
from model import *

class ErrorWindow(QDialog):
    def __init__(self, error_message):
        """ Initialisiere das Fenster """

        super().__init__()

        self.error_message = error_message

        self.color_green = "#5cb85c";
        self.color_red = "#d9534f";

        # Initialisiere die UI
        self.init_window_ui()

    # Allgemeine UI-Funktionen
    def init_window_ui (self):

        # Definiere Icons
        self.Icons["cancel"] = QIcon("res/img/cancel.png")

        message_label = QLabel(self.error_message)

        button = make_button(text = "OK", action = self.hide, height = full)

        # Initialisiere vertikales Layout
        self.vbox = QVBoxLayout()

        # Schrift für Buttons anpassen
        self.set_buttons_style("font-size: 25pt;")

        # Setze Layout für das Fenster
        self.setLayout(self.Layouts["vbox"])

    def set_buttons_style (self, style):
        css = "QPushButton { " + style + " }"
        self.setStyleSheet(css)

    def finish_ui (self):
        #self.Layouts["vbox"].addStretch()
        self.Layouts["vbox"].addLayout(self.Layouts["vboxnavbar"])
        self.show()

    def make_button (self, text, icon = "", action = None, height = 70, color = ""):
        """ Erstellt einen vordefinierten Button """
        button = QPushButton(text)
        if icon != "":
            button.setIcon(self.Icons[icon])
            button.setIconSize(QSize(50, 50))
        if action != None:
            button.clicked.connect(action)
        if height != "full":
            button.setFixedHeight(height)
        else:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if color != "":
            button.setStyleSheet("background-color:" + color + ";");
        return button
