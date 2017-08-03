from guis.scanui import *
from guis.window import *

class PayMethodCouponUI(ScanUI):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):

        self.Labels["information"].setText("Bitte legen Sie ihren Coupon auf das leuchtende Scannerfeld")


        self.add_cancel_button()

        self.finish_ui()
