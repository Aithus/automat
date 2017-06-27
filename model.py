from peewee import *

# Initialisiere DB
db = SqliteDatabase('data.db')

class AvailableTicket(Model):
    position = IntegerField()
    name = CharField()
    price = FloatField()

# Verbinde zur DB
db.connect()

# Erstelle Tabellen
db.create_tables([AvailableTicket], safe = True)

# Schließe Verbindung
db.close()
