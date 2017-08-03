from guis.window import *

class ScanUI(Window):
    def __init__(self, parent = None):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.Labels["information"] = QLabel()
        self.Layouts["vbox"].addWidget(self.Labels["information"])
        self.Labels["pic"] = QLabel()
        self.Layouts["vbox"].addWidget(self.Labels["pic"])

        self.TextEdits["eingabe"] = QTextEdit()
        self.Layouts["vbox"].addWidget(self.TextEdits["eingabe"])
