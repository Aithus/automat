from guis.window import *
from guis.selectticketsui import *
import sys

class StartUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def open_buy_ticket (self):
        stui = SelectTicketsUI(self)
        self.hide()

    def open_use_ticket (self):
        pass

    def init_ui(self):
        self.Buttons["buyticket"] = QPushButton("Ticket kaufen")
        self.Buttons["buyticket"].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Buttons["buyticket"].clicked.connect(self.open_buy_ticket)
        self.Layouts["vbox"].addWidget(self.Buttons["buyticket"])

        self.Buttons["useticket"] = QPushButton("Ticket einlösen")
        self.Buttons["useticket"].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Buttons["useticket"].clicked.connect(self.open_use_ticket)
        self.Layouts["vbox"].addWidget(self.Buttons["useticket"])
        self.finish_ui()
