from guis.window import *

class ScanUI(Window):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.add_cancel_button()

        self.finish_ui()
