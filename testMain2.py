# -*- coding: utf-8 -*-

import sys

from guis.selectpaymethodui import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = SelectPayMethodUI()

    sys.exit(app.exec_())
