from guis.window import *

class SelectTicketsUI(Window):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.Layouts["ticketgrid"] = QGridLayout()
        self.Buttons["tickets"] = {}

        names = ['A', 'B', 'C',
                'D', 'E', 'F',
                'G', 'H', 'I']

        positions = [(i,j) for i in range(3) for j in range(3)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            self.Buttons["tickets"][name] = QPushButton(name)
            self.Layouts["ticketgrid"].addWidget(self.Buttons["tickets"][name], *position)

        self.Layouts["vbox"].addLayout(self.Layouts["ticketgrid"])

        self.finish_ui()
