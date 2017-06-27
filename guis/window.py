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

        from settings import Settings
        self.Settings = Settings("config.json")

        self.init_window_ui()
        self.init_must_check()

    def init_window_ui (self):
        self.showFullScreen()

        self.Labels["title"] = QLabel(self.Settings.get("company_name"))
        self.Labels["time"] = QLabel("")
        self.update_time(self.Labels["time"])

        self.Layouts["hboxtitlebar"] = QHBoxLayout()
        self.Layouts["hboxtitlebar"].addWidget(self.Labels["title"])
        self.Layouts["hboxtitlebar"].addWidget(self.Labels["time"])

        self.Layouts["vbox"] = QVBoxLayout()
        self.Layouts["vbox"].addLayout(self.Layouts["hboxtitlebar"])
        self.setLayout(self.Layouts["vbox"])

    def update_time (self, time_label):
        import helper
        time = helper.get_time()
        time_label.setText(time)

    def init_must_check (self):
        self.WindowMustCheckTimer = QTimer()
        self.WindowMustCheckTimer.timeout.connect(self.must_check)
        self.WindowMustCheckTimer.start(100)

    def must_check (self):
        self.update_time(self.Labels["time"])
        self.WindowMustCheckTimer.start(100)
