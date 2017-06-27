# -*- coding: utf-8 -*-

import sys

from window import *
from startui import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = StartUI()

    sys.exit(app.exec_())
