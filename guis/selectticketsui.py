from guis.window import *

class SelectTicketsUI(Window):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['A', 'B', 'C',
                'D', 'E', 'F',
                'G', 'H', 'I']

        positions = [(i,j) for i in range(3) for j in range(3)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)
        
        self.show()
