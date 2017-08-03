from guis.window import *

class FinishUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):


        self.add_cancel_button()
        self.finish_ui()
