# -*- coding: utf-8 -*-

import sys

from guis.startui import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = StartUI()

    sys.exit(app.exec_())
