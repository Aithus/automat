from guis.window import *
from guis.checkticketsui import *

class SelectTicketsUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def next (self):
        ctui = CheckTicketsUI(self)
        self.hide()

    def get_available_tickets_formated (self):
        """ Gibt alle "verfügbaren" Tickets vorformatiert zurück """
        import model
        names = ['A', 'B', 'C',
                'D', 'E', 'F',
                'G', 'H', 'I']
        for ticket in model.AvailableTicket.select():
            names[ticket.position] = "" + ticket.name + "\n" + str(ticket.price) + " €"
        return names

    def add_to_cart (self):
        import time, model

        # Get ticket name
        sender_text = self.sender().text()
        ticket_name = sender_text.split("\n")[0]

        # Get ticket from available tickets per ticket name
        available_ticket = model.AvailableTicket.get(model.AvailableTicket.name == ticket_name)

        barcode = str(round(time.time()*100,0)).split(".")[0] + "00000000000"
        barcode = barcode[0:13]

        # Save ticket in cart
        if available_ticket != False:
            model.Ticket.create(barcode = barcode, ticket_type = available_ticket, cart = self.cart)
            self.Labels["info"].setText("<h1>Folgendes Ticket wurde dem Warenkorb hinzugefügt: " + ticket_name + "</h1>")

    def init_ui(self):
        # Create information label
        self.Labels["info"] = QLabel("<h1>Bitte wählen sie die gewünschten Tickets aus ...</h1>")

        # Create button grid
        self.Layouts["ticketgrid"] = QGridLayout()
        self.Buttons["tickets"] = {}

        # Get ticket names
        names = self.get_available_tickets_formated()

        # Create 3x3 grid
        positions = [(i,j) for i in range(3) for j in range(3)]

        # Add buttons to grid
        for position, name in zip(positions, names):

            if name == '':
                continue

            self.Buttons["tickets"][name] = self.make_button(text = name, height = "full", action = self.add_to_cart)
            self.Layouts["ticketgrid"].addWidget(self.Buttons["tickets"][name], *position)

        # Add widgets and layouts to the main layout
        self.Layouts["vbox"].addWidget(self.Labels["info"])
        self.Layouts["vbox"].addLayout(self.Layouts["ticketgrid"])

        self.add_cancel_button()
        self.add_next_button("Warenkorb ansehen")

        self.finish_ui()
