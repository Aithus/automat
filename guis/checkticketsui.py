from guis.window import *
from guis.selectpaymethodui import *

class CheckTicketsUI(Window):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def next (self):
        spmui = SelectPayMethodUI(self)
        self.hide()

    def get_ticket_list (self):
        """ Gibt einen Infostring für alle Tickets im Warenkorb zurück """

        import model

        tickets = []

        # Get all tickets in the cart
        for ticket in model.Ticket.select().where(model.Ticket.cart == self.cart):
            ticket_info = ticket.ticket_type.name + " > " + str(ticket.ticket_type.price) + " € (" + ticket.barcode + ")"
            tickets.append(ticket_info)

        return tickets

    def update_cart_list(self):
        """ Aktualisiert die Ticketliste im Warenkorb """

        self.OtherWidgets["cart_list"].clear()
        self.OtherWidgets["cart_list"].addItems(self.get_ticket_list())

    def update_total_price(self):
        """ Aktualisiert die Summe """

        total_price = self.cart.get_total_price()
        self.Labels["total_price"].setText("<h1>" + str(total_price) + " €</h1>")

    def delete_ticket(self):
        """ Löscht das aktuell ausgewählte Ticket """

        import model

        if (len(self.OtherWidgets["cart_list"].selectedItems()) > 0):
            # Get ticket barcode
            item = self.OtherWidgets["cart_list"].selectedItems()[0].text()
            ticket = item.split("(")[1].replace(")", "")

            if self.OtherWidgets["cart_list"].count() > 1:
                # Delete ticket
                query = model.Ticket.delete().where(model.Ticket.barcode == ticket, model.Ticket.cart == self.cart)
                query.execute()
                self.Labels["info2"].setText("<h2>Das Ticket wurde erfolgreich entfernt!</h2>")
            else:
                self.Labels["info2"].setText("<h2>Sie müssen mindestens ein Ticket im Warenkorb haben!</h2>")

        # Update view
        self.update_cart_list()
        self.update_total_price()

    def init_ui(self):
        """ Initialisiert die UI """

        # Create information label
        self.Labels["info"] = QLabel("<h1>Bitte überprüfen Sie ihre Tickets ...</h1>")
        self.Labels["info2"] = QLabel("<h3>Wenn Sie ein Element entfernen wollen, wählen Sie es aus und drücken auf 'Ticket entfernen', wenn alles stimmt, drücken Sie auf 'Bezahlen'!</h3>")

        # Create list view
        self.OtherWidgets["cart_list"] = QListWidget()
        self.OtherWidgets["cart_list"].setStyleSheet("font-size: 30px;")
        self.update_cart_list()

        # Create total price label
        self.Labels["info_total_price"] = QLabel("<h1>Summe</h1>")
        self.Labels["total_price"] = QLabel("")
        self.Labels["total_price"].setAlignment(Qt.AlignRight)
        self.update_total_price()

        self.Layouts["total_price"] = QHBoxLayout()
        self.Layouts["total_price"].addWidget(self.Labels["info_total_price"])
        self.Layouts["total_price"].addWidget(self.Labels["total_price"])

        # Create delete button
        self.Buttons["delete_ticket"] = self.make_button("Ticket entfernen", icon = "cancel", height = 70, action = self.delete_ticket, color = self.color_red)

        # Add widgets and layouts to the main layout
        self.Layouts["vbox"].addWidget(self.Labels["info"])
        self.Layouts["vbox"].addWidget(self.Labels["info2"])

        self.Layouts["vbox"].addWidget(self.OtherWidgets["cart_list"])

        self.Layouts["vbox"].addLayout(self.Layouts["total_price"])

        self.Layouts["vbox"].addWidget(self.Buttons["delete_ticket"])

        self.add_cancel_button()
        self.add_next_button("Bezahlen")

        self.finish_ui()
