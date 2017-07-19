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
    total_price = FloatField(default = 0)
    pay = ForeignKeyField(Pay, related_name = "cart", null = True)

class Ticket(Model):
    barcode = CharField()
    used = BooleanField(default = False)
    ticket_type = ForeignKeyField(AvailableTicket)
    cart = ForeignKeyField(Cart, related_name = "tickets")

# Verbinde zur DB
db.connect()

# Erstelle Tabellen
db.create_tables([AvailableTicket, Pay, Ticket, Cart], safe = True)

# Schließe Verbindung
db.close()
