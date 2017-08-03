from peewee import *
import datetime

# Initialisiere DB
db = SqliteDatabase('data/data.db')

# Initialisiere Modelle
class Pay(Model):
    method = IntegerField()
    payed_at = DateTimeField(default = datetime.datetime.now)

class AvailableTicket(Model):
    position = IntegerField()
    name = CharField()
    price = FloatField()

class Cart(Model):
    created_at = DateTimeField(default = datetime.datetime.now)
    pay = ForeignKeyField(Pay, related_name = "cart", null = True)

    def get_total_price(self):
        """ Gibt die Summe des Warenkorbs zurück """

        total_price = 0
        for ticket in Ticket.select().where(Ticket.cart == self):
            total_price += ticket.ticket_type.price
        return total_price

class Ticket(Model):
    barcode = CharField()
    used = BooleanField(default = False)
    ticket_type = ForeignKeyField(AvailableTicket)
    cart = ForeignKeyField(Cart, related_name = "tickets")

class Device(Model):
    name = CharField()

class Message(Model):
    message = CharField()
    device = ForeignKeyField(Device, related_name = "messages"e)

    def send(self, message, device):
        Message.create(message = message, device = device)

    def has(self, message, device):
        for msg in Message.select().where(Message.device = device):
            if msg.message == message:
                return True
                msg.delete()
        return False

# Verbinde zur DB
db.connect()

# Erstelle Tabellen
db.create_tables([AvailableTicket, Pay, Ticket, Cart], safe = True)

# Schließe Verbindung
db.close()
