from guis.window import *
from guis.errorwindow import *

class PayMethodCouponUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def get_coupon(self, barcode):
        import model

        money_on_coupon = 0.0
        activated = False
        price = self.cart.get_total_price()
        for coupon in model.Coupon.select().where(model.Coupon.barcode == barcode):
            activated = coupon.available
            money_on_coupon = coupon.value
            break

        if activated != False:
            if money_on_coupon >= price:
            else:
                ErrorWindow("Fehlermeldung")
        else:
            # Error
            pass

    def do (self):
        barcode = self.TextEdits["eingabe"].text()
        if len(barcode) == 13:
            self.TextEdits["eingabe"].clear()
            self.get_coupon(barcode)

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
        self.TextEdits["eingabe"].textChanged.connect(self.do)
