from guis.window import *

class SelectTicketsUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

    def get_available_tickets (self):
        import model
        names = ['A', 'B', 'C',
                'D', 'E', 'F',
                'G', 'H', 'I']
        for ticket in model.AvailableTicket.select():
            names[ticket.position] = "" + ticket.name + "\n" + str(ticket.price) + " €"
        return names

    def add_to_cart (self):
        sender_text = self.sender().text()
        self.Labels["info"].setText(sender_text)

    def init_ui(self):
        self.Labels["info"] = QLabel("<h1>Bitte wählen sie die gewünschten Tickets aus ...</h1>")

        self.Layouts["ticketgrid"] = QGridLayout()
        self.Buttons["tickets"] = {}

        names = self.get_available_tickets()

        positions = [(i,j) for i in range(3) for j in range(3)]

        for position, name in zip(positions, names):

            if name == '':
                continue

            self.Buttons["tickets"][name] = QPushButton(name)
            self.Buttons["tickets"][name].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.Buttons["tickets"][name].clicked.connect(self.add_to_cart)

            self.Layouts["ticketgrid"].addWidget(self.Buttons["tickets"][name], *position)

        self.Layouts["vbox"].addWidget(self.Labels["info"])
        self.Layouts["vbox"].addLayout(self.Layouts["ticketgrid"])

        self.add_cancel_button()
        self.add_next_button("Warenkorb ansehen")

        self.finish_ui()
