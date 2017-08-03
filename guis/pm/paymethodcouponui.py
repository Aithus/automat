from guis.window import *
import guis.errorwindow as ew

class PayMethodCouponUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def get_coupon(self, barcode):
        import model

        exist = False;
        money_on_coupon = 0.0
        activated = False
        price = self.cart.get_total_price()
        for coupon in model.Coupon.select().where(model.Coupon.barcode == barcode):
            activated = coupon.available
            money_on_coupon = coupon.value
            exist = True;
            break

        if exist == False:
            msg_box = QMessageBox.about(self, "Fehler", "Ihre Gutscheinkarte funktioniert leider nicht. Bitte benutzen Sie eine andere Karte oder rufen Sie einen Mitarbeiter.")

        if activated != False:
            if money_on_coupon >= price:
                pass
            else:
                print("FEHLER")
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Critical)
                msg_box.setText("Sie haben zu wenig Guthaben auf ihrer Gutscheinkarte. Bitte fügen Sie weitere Karten hinzu oder nutzen Sie eine andere Zahlungsmethode.")
                msg_box.exec_()
        else:
            # Error
            pass

    def do (self):
        barcode = self.TextEdits["eingabe"].text()
        if len(barcode) == 13:
            self.TextEdits["eingabe"].clear()
            self.get_coupon(barcode)

    def init_ui(self):

        self.Labels["info"] = QLabel("<h1>Bitte legen Sie ihren Gutschein auf das leuchtende Scannerfeld:</h1>")
        self.Layouts["vbox"].addWidget(self.Labels["info"])
        self.Labels["pic"] = QLabel()
        self.Layouts["vbox"].addWidget(self.Labels["pic"])

        self.TextEdits["eingabe"] = QLineEdit()
        self.Layouts["vbox"].addWidget(self.TextEdits["eingabe"])

        self.add_cancel_button()

        self.finish_ui()

        self.TextEdits["eingabe"].grabKeyboard()
        self.TextEdits["eingabe"].textChanged.connect(self.do)
