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
        self.Buttons["buyticket"] = self.make_button(text = "Ticket kaufen", action = self.open_buy_ticket, height = "full")
        self.Layouts["vbox"].addWidget(self.Buttons["buyticket"])

        self.Buttons["useticket"] = self.make_button(text = "Ticket einlösen", action = self.open_use_ticket, height = "full")
        self.Layouts["vbox"].addWidget(self.Buttons["useticket"])
        
        self.finish_ui()
