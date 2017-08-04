from guis.window import *
from guis.finishui import *

class PayMethodCouponUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def get_coupon(self, barcode):
        import model

        price = self.cart.get_total_price()

        exist = False;
        for coupon in model.Coupon.select().where(model.Coupon.barcode == barcode):
            exist = True
            break

        # Error Code: 001 = Karte nicht aktiviert; 002 = Zu wenig Guthaben; 003 = Gutscheinkarte existiert im System nicht

        if exist == False: # existiert
            msg_003 = "Ihre Gutscheinkarte funktioniert leider nicht. Bitte benutzen Sie eine andere Karte oder rufen Sie einen Mitarbeiter. (Fehlercode 003)"
            msg_box = QMessageBox.about(self, "Fehler", msg_003)
            # Funktion verlassen
        else:
            if coupon.available != False: # aktiviert
                if coupon.value >= price: # genügend Guthaben vorhanden
                    # Neuen Gutscheinwert berechnen
                    coupon.value -= price
                    coupon.save()

                    # Zahlung eintragen
                    pay = model.Pay.create(method = PAY_METHOD_COUPON, method_barcode = coupon.barcode)
                    self.cart.pay = pay
                    self.cart.save()

                    # Druckoberfläche starten
                    fnui = FinishUI(self, PAY_METHOD_COUPON, coupon.value)
                    self.hide()

                else: # Zu wenig Guthaben
                    msg_002 = "Sie haben zu wenig Guthaben auf ihrer Gutscheinkarte. Bitte fügen Sie weitere Karten hinzu oder nutzen Sie eine andere Zahlungsmethode. Ihr derzeitiger Kontostand beträgt " + str(coupon.value) + " €. (Fehlercode 002)"
                    msg_box = QMessageBox.about(self, "Fehler", msg_002)
            else: # Nicht aktiviert
                msg_001 = "Ihre Gutscheinkarte ist nicht aktiviert. Bitte rufen Sie einen Mitarbeiter oder benutzen Sie eine andere Karte. (Fehlercode 001)"
                msg_box = QMessageBox.about(self, "Fehler", msg_001)

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
        self.Layouts["vbox"].addStretch()
        self.add_cancel_button()

        self.finish_ui()

        self.TextEdits["eingabe"].grabKeyboard()
        self.TextEdits["eingabe"].textChanged.connect(self.do)
