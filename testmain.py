# -*- coding: utf-8 -*-

import sys

from guis.errorwindow import *

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # Zeige Fenster
    startui = ErrorWindow(self, "Fehlermeldung")

    sys.exit(app.exec_())
