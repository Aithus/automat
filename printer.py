class Printing():
    def __init__(self):
        self.width = 58
        self.height = 87
        from fpdf import FPDF
        self.pdf = FPDF("P", "mm", [self.width, self.height])

    def create_barcode(self, barcode):
        import os
        os.system("./barcode.sh " + barcode)
        return "/tmp/barcode.png"

    def create_ticket(self):
        barcode = self.create_barcode('123456789102')

        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 20)
        self.pdf.cell(40, 10, 'TICKET', align = "C")
        self.pdf.ln(10)

        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(40, 10, 'Seniorenticket')

        self.pdf.ln(5)
        self.pdf.cell(40, 10, '30 EUR', align = "R")

        self.pdf.ln(10)
        self.pdf.image(barcode, w = 40, h = 10)

        self.pdf.ln(10)
        self.pdf.cell(40, 10, "--", align = "C")

        self.pdf.output('ticket.pdf', 'F')

        return "ticket.pdf"

    def do(self, filename):
        import os
        os.system("lpr " + filename)
