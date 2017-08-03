# -*- coding: utf-8 -*-

import sys

from guis.scanui import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = ScanUI()

    sys.exit(app.exec_())
