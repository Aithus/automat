from guis.window import *

class CheckTicketsUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def get_ticket_list (self):
        """ Gibt einen Infostring für alle Tickets im Warenkorb zurück """
        import model

        tickets = []

        # Get all tickets in the cart
        for ticket in model.Ticket.select().where(model.Ticket.cart == self.cart):
            ticket_info = ticket.ticket_type.name + " > " + str(ticket.ticket_type.price) + " €"
            tickets.append(ticket_info)

        return tickets

    def update_cart_list(self):
        self.OtherWidgets["cart_list"].clear()
        self.OtherWidgets["cart_list"].addItems(self.get_ticket_list())

    def delete_ticket(self):
        """ Löscht das aktuell ausgewählte Ticket """
        import model

        item = self.OtherWidgets["cart_list"].selectedItems()[0].text()
        ticket = item.split(" >")[0]

        print("+"+ticket+"+")
        # if nicht zu viel
        model.Ticket.delete().where(model.Ticket.ticket_type.name == ticket, model.Ticket.cart == self.cart)
        self.update_cart_list()

    def init_ui(self):
        # Create information label
        self.Labels["info"] = QLabel("<h1>Bitte überprüfen Sie ihre Tickets ...</h1>")
        self.Labels["info2"] = QLabel("<h3>Wenn Sie ein Element entfernen wollen, wählen Sie es aus und drücken auf 'Ticket entfernen', wenn alles stimmt, drücken Sie auf 'Bezahlen'!</h3>")

        # Create list view
        self.OtherWidgets["cart_list"] = QListWidget()
        self.OtherWidgets["cart_list"].setStyleSheet("font-size: 30px;")
        self.update_cart_list()

        # Create delete button
        self.Buttons["delete_ticket"] = self.make_button("Ticket entfernen", icon = "cancel", height = 70, action = self.delete_ticket, color = self.color_red)

        # Add widgets and layouts to the main layout
        self.Layouts["vbox"].addWidget(self.Labels["info"])
        self.Layouts["vbox"].addWidget(self.Labels["info2"])

        self.Layouts["vbox"].addWidget(self.OtherWidgets["cart_list"])

        self.Layouts["vbox"].addWidget(self.Buttons["delete_ticket"])

        self.add_cancel_button()
        self.add_next_button("Bezahlen")

        self.finish_ui()
