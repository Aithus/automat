from guis.scanui import *
from guis.window import *

class PayMethodCouponUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):

        self.Labels["information"] = QLabel("<h1>Bitte legen Sie ihren Gutschein auf das leuchtende Scannerfeld:</h1>")
        self.Layouts["vbox"].addWidget(self.Labels["information"])
        self.Labels["pic"] = QLabel()
        self.Layouts["vbox"].addWidget(self.Labels["pic"])

        self.TextEdits["eingabe"] = QLineEdit()
        self.Layouts["vbox"].addWidget(self.TextEdits["eingabe"])

##        self.TextEdits["eingabe"] = QTextEdit()
##        self.Layouts["vbox"].addWidget(self.TextEdits["eingabe"])
##        self.TextEdits["eingabe"].setFocus()

        self.add_cancel_button()

        self.finish_ui()

        self.TextEdits["eingabe"].grabKeyboard()

        self.update()
