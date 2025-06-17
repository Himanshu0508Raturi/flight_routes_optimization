# seed_data.py
from pymongo import MongoClient

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Access your MongoDB URI
MONGO_URI = os.getenv("MONGODB_URI")

# Example: use it with pymongo
client = MongoClient(MONGO_URI)
db = client["flightdb"]

# Insert Airports
airports = ['DEL', 'BOM', 'BLR', 'MAA', 'HYD', 'CCU', 'AMD', 'GOI', 'PAT', 'PNQ', 'TRV', 'STV', 'VGA', 'IXC', 'JAI']
db.airports.drop()
db.airports.insert_many([{"code": code} for code in airports])

# Insert Routes
edges = [
    {'source': 'DEL', 'dest': 'BOM', 'Cost': 4500, 'Distance': 1400, 'Time': 2.0},
    {'source': 'BOM', 'dest': 'JAI', 'Cost': 3200, 'Distance': 1100, 'Time': 1.8},
    {'source': 'BLR', 'dest': 'JAI', 'Cost': 5500, 'Distance': 1600, 'Time': 2.3},
    {'source': 'MAA', 'dest': 'BLR', 'Cost': 2200, 'Distance': 350,  'Time': 1.0},
    {'source': 'PNQ', 'dest': 'GOI', 'Cost': 2100, 'Distance': 500,  'Time': 1.1},
    {'source': 'AMD', 'dest': 'GOI', 'Cost': 2400, 'Distance': 650,  'Time': 1.2},
    {'source': 'CCU', 'dest': 'HYD', 'Cost': 4600, 'Distance': 1450, 'Time': 2.1},
    {'source': 'CCU', 'dest': 'MAA', 'Cost': 2800, 'Distance': 1350, 'Time': 1.9},
    {'source': 'MAA', 'dest': 'DEL', 'Cost': 4700, 'Distance': 1700, 'Time': 2.5},
    {'source': 'DEL', 'dest': 'TRV', 'Cost': 5000, 'Distance': 1800, 'Time': 2.7},
    {'source': 'AMD', 'dest': 'CCU', 'Cost': 2300, 'Distance': 1600, 'Time': 2.2},
    {'source': 'IXC', 'dest': 'JAI', 'Cost': 2500, 'Distance': 800,  'Time': 1.3},
    {'source': 'DEL', 'dest': 'STV', 'Cost': 4100, 'Distance': 1500, 'Time': 2.0},
    {'source': 'STV', 'dest': 'VGA', 'Cost': 3900, 'Distance': 1400, 'Time': 1.8},
    {'source': 'VGA', 'dest': 'IXC', 'Cost': 5200, 'Distance': 1700, 'Time': 1.4},
    {'source': 'TRV', 'dest': 'STV', 'Cost': 5300, 'Distance': 1750, 'Time': 2.5},
    {'source': 'HYD', 'dest': 'BLR', 'Cost': 3000, 'Distance': 600,  'Time': 1.2},
    {'source': 'PNQ', 'dest': 'PAT', 'Cost': 4900, 'Distance': 1600, 'Time': 2.3},
    {'source': 'PAT', 'dest': 'TRV', 'Cost': 5200, 'Distance': 1800, 'Time': 2.6},
    {'source': 'PAT', 'dest': 'DEL', 'Cost': 4700, 'Distance': 1500, 'Time': 2.2},
    {'source': 'MAA', 'dest': 'PNQ', 'Cost': 3500, 'Distance': 1200, 'Time': 1.7},
    {'source': 'GOI', 'dest': 'MAA', 'Cost': 3400, 'Distance': 1000, 'Time': 1.5},
    {'source': 'BOM', 'dest': 'VGA', 'Cost': 2400, 'Distance': 500, 'Time': 1},
]
db.routes.drop()
db.routes.insert_many(edges)

print("MongoDB seeded successfully.")
