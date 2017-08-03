from guis.window import *
from guis.pm.paymethodcouponui import *
from guis.pm.paymethodcreditcardui import *
from guis.pm.paymethodcashui import *

class SelectPayMethodUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def open_cash(self):
        msg_box = QMessageBox.about(self, "Fehler", "Diese Zahlungsmethode wird aktuell noch nicht unterstützt. Bitte wählen Sie eine andere.")

    def open_credit_card(self):
        pmcd = PayMethodCreditCardUI(self)
        self.hide()

    def open_coupon(self):
        pmc = PayMethodCouponUI(self)
        self.hide()

    def init_ui(self):
        self.Buttons["cash"] = self.make_button(text = "Barzahlung mit Scheinen", action = self.open_cash, height = "full", icon = "cash")
        self.Layouts["vbox"].addWidget(self.Buttons["cash"])

        self.Buttons["credit_card"] = self.make_button(text = "Zahlung mit Kreditkarte", action = self.open_credit_card, height = "full", icon = "credit_card")
        self.Layouts["vbox"].addWidget(self.Buttons["credit_card"])

        self.Buttons["coupon"] = self.make_button(text = "Gutschein einlösen", action = self.open_coupon, height = "full", icon = "coupon")
        self.Layouts["vbox"].addWidget(self.Buttons["coupon"])

        self.add_cancel_button()

        self.finish_ui()
