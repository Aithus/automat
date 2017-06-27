from model import *

ticketnames = ["Normales Ticket", "Kinderticket", "Seniorenticket",
                "Freikarte", "VIP-Ticket", "Familienticket",
                "Backstageticket", "Schwerbehindertenticket", "Haustierticket"]

ticketprices = [10, 7, 8.5,
                0, 20, 30,
                30, 2.5, 3]

for i in range(0,9):
    ticketname = ticketnames[i]
    ticketprice = ticketprices[i]

    AvailableTicket.create(position = i, name = ticketname, price = ticketprice)
