# seed_data.py
from pymongo import MongoClient

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Access your MongoDB URI
MONGO_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGO_URI)
db = client["flightdb"]

# Insert Airports
airports = ['DEL', 'BOM', 'BLR', 'MAA', 'HYD', 'CCU', 'AMD', 'GOI', 'PAT', 'PNQ', 'TRV', 'STV', 'VGA', 'IXC', 'JAI']
#db.airports.drop()


# Insert Routes
edges = [
    {"source": "DEL", "destination": "BOM", "distance": 1400, "cost": 4500, "time": 2.0},
    {"source": "BOM", "destination": "JAI", "distance": 1100, "cost": 3200, "time": 1.8},
    {"source": "BLR", "destination": "JAI", "distance": 1600, "cost": 5500, "time": 2.3},
    {"source": "MAA", "destination": "BLR", "distance": 350, "cost": 2200, "time": 1.0},
    {"source": "PNQ", "destination": "GOI", "distance": 500, "cost": 2100, "time": 1.1},
    {"source": "AMD", "destination": "GOI", "distance": 650, "cost": 2400, "time": 1.2},
    {"source": "CCU", "destination": "HYD", "distance": 1450, "cost": 4600, "time": 2.1},
    {"source": "CCU", "destination": "MAA", "distance": 1350, "cost": 2800, "time": 1.9},
    {"source": "MAA", "destination": "DEL", "distance": 1700, "cost": 4700, "time": 2.5},
    {"source": "DEL", "destination": "TRV", "distance": 1800, "cost": 5000, "time": 2.7},
    {"source": "AMD", "destination": "CCU", "distance": 1600, "cost": 2300, "time": 2.2},
    {"source": "IXC", "destination": "JAI", "distance": 800, "cost": 2500, "time": 1.3},
    {"source": "DEL", "destination": "STV", "distance": 1500, "cost": 4100, "time": 2.0},
    {"source": "STV", "destination": "VGA", "distance": 1400, "cost": 3900, "time": 1.8},
    {"source": "VGA", "destination": "IXC", "distance": 1700, "cost": 5200, "time": 1.4},
    {"source": "TRV", "destination": "STV", "distance": 1750, "cost": 5300, "time": 2.5},
    {"source": "HYD", "destination": "BLR", "distance": 600, "cost": 3000, "time": 1.2},
    {"source": "PNQ", "destination": "PAT", "distance": 1600, "cost": 4900, "time": 2.3},
    {"source": "PAT", "destination": "TRV", "distance": 1800, "cost": 5200, "time": 2.6},
    {"source": "PAT", "destination": "DEL", "distance": 1500, "cost": 4700, "time": 2.2},
    {"source": "MAA", "destination": "PNQ", "distance": 1200, "cost": 3500, "time": 1.7},
    {"source": "GOI", "destination": "MAA", "distance": 1000, "cost": 3400, "time": 1.5},
    {"source": "BOM", "destination": "VGA", "distance": 500, "cost": 2400, "time": 1.0},
]

#db.routes.drop()
db.edges.insert_many(edges)

print("MongoDB seeded successfully.")