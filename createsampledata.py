from model import *

ticketnames = ["Normales Ticket", "Kinderticket", "Seniorenticket",
                "Freikarte", "VIP-Ticket", "Familienticket",
                "Backstageticket", "Schwerbehindertenticket", "Haustierticket"]

ticketprices = [10, 7, 8.5,
                0, 20, 30,
                30, 2.5, 3]

couponMoney = [30, 30, 30,
                    10, 10, 10,
                    10, 10, 10]

couponsAvailable = [1, 0, 1,
                    0, 1, 0,
                    1, 0, 1]

barcodes = [9951145210445, 9951145213866, 9951145210452,
            2408063017320, 2408056804241, 2408063017382,
            2408063017412, 2408051508069, 2408051508052]

for i in range(0,9):
    money = couponMoney[i]
    couponAvailable = couponsAvailable[i]
    couponBarcode = barcodes[i]

    Coupon.create(position = i, barcode = couponBarcode, value = money, cAvailable = couponAvailable)

for i in range(0,9):
    ticketname = ticketnames[i]
    ticketprice = ticketprices[i]

    AvailableTicket.create(position = i, name = ticketname, price = ticketprice)
