class Printing():
    def __init__(self):
        self.width = 58
        self.height = 87
        from fpdf import FPDF
        self.pdf = FPDF("P", "mm", [self.width, self.height])

    def create_ticket(self):
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 20)
        self.pdf.cell(40, 10, 'TICKET', align = "C")
        self.pdf.ln(10)

        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(40, 10, 'Seniorenticket')

        self.pdf.ln(5)
        self.pdf.cell(40, 10, '30 EUR', align = "R")
        self.pdf.output('test.pdf', 'F')
