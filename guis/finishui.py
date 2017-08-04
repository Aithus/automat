from guis.window import *

class FinishUI(Window):
    def __init__(self, parent = None, pay_method = 0, coupon_value = 0):
        super().__init__(parent)
        self.init_ui(pay_method, coupon_value)

    def do_printing(self):
        pass


    def init_ui(self, pay_method, new_value):
        if (pay_method == PAY_METHOD_COUPON):
            msg = "<h2>Ihre Zahlung ist erfolgreich ausgeführt worden. Ihre Gutscheinkarte hat nun einen Kontostand von " + str(new_value) + " €.</h2>"
        else:
            msg = "<h2>Ihre Zahlung ist erfolgreich ausgeführt worden.</h2>"

        self.Labels["success"] = QLabel(msg)
        self.Layouts["vbox"].addWidget(self.Labels["success"])

        self.Labels["BorderLine3"] = QLabel("<hr>")
        self.Layouts["vbox"].addWidget(self.Labels["BorderLine3"])

        self.Labels["print"] = QLabel("<h1>Ihre Tickets werden nun gedruckt. Bitte gedulden Sie sich einen Moment.</h1>")
        self.Layouts["vbox"].addWidget(self.Labels["print"])

        self.Layouts["vbox"].addStretch()

        self.add_cancel_button()
        self.finish_ui()
