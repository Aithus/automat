# -*- coding: utf-8 -*-

import sys

from guis.paymethodcouponui import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = PayMethodCouponUI()

    sys.exit(app.exec_())
