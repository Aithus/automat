# -*- coding: utf-8 -*-

import sys

from guis.selectticketsui import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = SelectTicketsUI()

    sys.exit(app.exec_())
