from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication)
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

    def init_ui (self):
        self.showFullScreen()
        self.Labels["title"] = QLabel("Anzahl der Würfelvorgänge")
        self.Layouts["vbox"] = QVBoxLayout()

    def center(self):
        """ Zentriert das Fenster """

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
