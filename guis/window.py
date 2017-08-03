from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget,
    QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QLabel, QListWidget,
    QMessageBox,
    QApplication, QDialog,
    QGridLayout, QSizePolicy)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import *
from model import *

class Window(QDialog):
    def __init__(self, parent = None, cart_activated = True):
        """ Initialisiere das Fenster """

        super().__init__(parent)
        self.Labels = {}
        self.Buttons = {}
        self.Edits = {}
        self.Layouts = {}
        self.Icons = {}
        self.OtherWidgets = {}

        self.color_green = "#5cb85c";
        self.color_red = "#d9534f";

        self.cart = None
        self.cart_activated = cart_activated

        # Importiere die Einstellungen
        from settings import Settings
        self.Settings = Settings("config.json")

        # Lege Warenkorb fest
        if self.cart_activated:
            if parent != None:
                if parent.cart != None:
                    self.cart = parent.cart
                else:
                    self.create_cart()
            else:
                self.create_cart()

        # Initialisiere die UI und den Mainloop
        self.init_window_ui()
        self.init_must_check()

    # Allgemeine UI-Funktionen
    def init_window_ui (self):
        # Zeige das Fenster im Vollbild
        self.showFullScreen()

        # Definiere eine vorgefertigte Linie
        self.BorderLine = QLabel("<hr>")
        self.BorderLine2 = QLabel("<hr>")

        # Definiere Icons
        self.Icons["cancel"] = QIcon("res/img/cancel.png")
        self.Icons["left"] = QIcon("res/img/left.png")
        self.Icons["right"] = QIcon("res/img/right.png")
        self.Icons["cash"] = QIcon("res/img/cash.png")
        self.Icons["coupon"] = QIcon("res/img/coupon.png")
        self.Icons["credit_card"] = QIcon("res/img/credit_card.png")
        
        # Definiere Labels für Titelleiste
        self.Labels["title"] = QLabel("<h1>" + self.Settings.get("company_name") + "</h1>")
        self.Labels["title"].setAlignment(Qt.AlignLeft)
        self.Labels["time"] = QLabel("")
        self.Labels["time"].setAlignment(Qt.AlignRight)
        self.update_time(self.Labels["time"])

        # Füge die Titelleiste hinzu
        self.Layouts["hboxtitlebar"] = QHBoxLayout()
        self.Layouts["hboxtitlebar"].addWidget(self.Labels["title"])
        self.Layouts["hboxtitlebar"].addWidget(self.Labels["time"])

        self.Layouts["vboxtitlebar"] = QVBoxLayout()
        self.Layouts["vboxtitlebar"].addLayout(self.Layouts["hboxtitlebar"])
        self.Layouts["vboxtitlebar"].addWidget(self.BorderLine)

        # Füge Navigationsleiste hinzu
        self.Layouts["hboxnavbar"] = QHBoxLayout()

        self.Layouts["vboxnavbar"] = QVBoxLayout()
        self.Layouts["vboxnavbar"].addWidget(self.BorderLine2)
        self.Layouts["vboxnavbar"].addLayout(self.Layouts["hboxnavbar"])

        # Initialisiere vertikales Layout
        self.Layouts["vbox"] = QVBoxLayout()
        self.Layouts["vbox"].addLayout(self.Layouts["vboxtitlebar"])
        # self.Layouts["vbox"].addStretch()

        # Schrift für Buttons anpassen
        self.set_buttons_style("font-size: 25pt;")

        # Setze Layout für das Fenster
        self.setLayout(self.Layouts["vbox"])

    def set_buttons_style (self, style):
        css = "QPushButton { " + style + " }"
        self.setStyleSheet(css)

    def finish_ui (self):
        #self.Layouts["vbox"].addStretch()
        self.Layouts["vbox"].addLayout(self.Layouts["vboxnavbar"])
        self.show()

    def make_button (self, text, icon = "", action = None, height = 70, color = ""):
        """ Erstellt einen vordefinierten Button """
        button = QPushButton(text)
        if icon != "":
            button.setIcon(self.Icons[icon])
            button.setIconSize(QSize(50, 50))
        if action != None:
            button.clicked.connect(action)
        if height != "full":
            button.setFixedHeight(height)
        else:
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if color != "":
            button.setStyleSheet("background-color:" + color + ";");
        return button

    # Navigationsleiste
    def cancel (self):
        self.close()

    def add_cancel_button (self, text = "Abbrechen"):
        self.Buttons["cancel"] = self.make_button(text = text, icon = "cancel", action = self.cancel, color = self.color_red)
        self.Layouts["hboxnavbar"].addWidget(self.Buttons["cancel"])

    def back (self):
        pass

    def add_back_button (self, text = "Zurück"):
        self.Buttons["back"] = self.make_button(text = text, icon = "left", action = self.back)
        self.Layouts["hboxnavbar"].addWidget(self.Buttons["back"])

    def next (self):
        pass

    def add_next_button(self, text = "Weiter"):
        self.Buttons["next"] = self.make_button(text = text, icon = "right", action = self.next, color = self.color_green)
        self.Layouts["hboxnavbar"].addWidget(self.Buttons["next"])

    # Warenkorb
    def create_cart (self):
        self.cart = Cart()
        self.cart.save()

    def update_cart (self):
        self.cart.save()

    # Uhrzeitfunktionen
    def update_time (self, time_label):
        """ Aktualisiert die Zeit in einem Label """
        import helper
        time = helper.get_time()
        time_label.setText("<h1>" + time + "</h1>")

    def init_must_check (self):
        """ Initialisert einen "Mainloop" """
        self.WindowMustCheckTimer = QTimer()
        self.WindowMustCheckTimer.timeout.connect(self.must_check)
        self.WindowMustCheckTimer.start(100)

    def must_check (self):
        """ Führt den Mainloop durch """
        self.update_time(self.Labels["time"])
        if self.cart_activated:
            self.update_cart()
        self.WindowMustCheckTimer.start(100)
        self.updated_must_check()

    def updated_must_check (self):
        pass
