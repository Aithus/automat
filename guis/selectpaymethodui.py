from guis.window import *

class SelectPayMethodUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def open_cash(self):
        pass

    def open_credit_card(self):
        pass

    def open_coupon(self):
        pass

    def init_ui(self):
        self.Buttons["cash"] = self.make_button(text = "Barzahlung mit Scheinen", action = self.open_cash, height = "full")
        self.Layouts["vbox"].addWidget(self.Buttons["cash"])

        self.Buttons["credit_card"] = self.make_button(text = "Ticket einlösen", action = self.open_credit_card, height = "full")
        self.Layouts["vbox"].addWidget(self.Buttons["credit_card"])

        self.Buttons["coupon"] = self.make_button(text = "Ticket einlösen", action = self.open_coupon, height = "full")
        self.Layouts["vbox"].addWidget(self.Buttons["coupon"])

        self.add_cancel_button()

        self.finish_ui()
