from guis.window import *

class SelectTicketsUI(Window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_ui()

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
        sender_text = self.sender().text()
        ticket_name = sender_text.split("\n")[0]
        self.Labels["info"].setText(ticket_name)

    

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
