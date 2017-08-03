from guis.window import *

class FinishUI(Window):
    def __init__(self, parent = None, coupon_value = 0):
        super().__init__(parent)
        self.init_ui(coupon_value)


    def init_ui(self, coupon_value):
        self.Labels["success"] = QLabel("Ihre Zahlung ist erfolgreich ausgeführt worden. Ihre Gutscheinkarte hat nun einen Kontostand von " + str(coupon_value) + " €.")
        self.Layouts["vbox"].addWidget(self.Labels["success"])

        self.add_cancel_button()
        self.finish_ui()
