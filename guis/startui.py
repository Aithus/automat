from PyQt5.QtWidgets import (QWidget, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel,
    QMessageBox,
    QApplication)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *

from window import *

class StartUI(Window):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.Labels["anzahl"] = QLabel("Anzahl der Würfelvorgänge")
        self.Edits["anzahl"] = QLineEdit("1000")

        self.Buttons["start"] = QPushButton("Würfeln")
        self.Buttons["start"].setToolTip("Klicke auf diesen Button, um den <b>Würfelvorgang</b> zu starten")
        #self.Buttons["start"].clicked.connect()

        # Layouts
        self.Layouts["hbox1"] = QHBoxLayout()
        self.Layouts["hbox1"].addWidget(self.Labels["anzahl"])
        self.Layouts["hbox1"].addWidget(self.Edits["anzahl"])

        self.Layouts["vbox"] = QVBoxLayout()
        self.Layouts["vbox"].addLayout(self.Layouts["hbox1"])
        self.Layouts["vbox"].addWidget(self.Buttons["start"])

        self.setLayout(self.Layouts["vbox"])

        # Aussehen und Position
        self.center()

        self.setWindowTitle("Würfel")
        self.setWindowIcon(QIcon("wuerfelicon-small.png"))

        # Zeigen
        self.show()
