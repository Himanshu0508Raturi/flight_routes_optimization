from pymongo import MongoClient

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Access your MongoDB URI
MONGO_URI = os.getenv("MONGODB_URI")

# Example: use it with pymongo
from pymongo import MongoClient
client = MongoClient(MONGO_URI)

db = client["flightdb"]

# Create or select collection
collection = db["Kruskal_nodes"]

# Full airport data
airports_data = [
    {"from": "DEL", "to": "BOM", "distance": 1150, "fuel_cost": 50000},
    {"from": "DEL", "to": "BLR", "distance": 1750, "fuel_cost": 75000},
    {"from": "DEL", "to": "HYD", "distance": 1250, "fuel_cost": 55000},
    {"from": "BOM", "to": "BLR", "distance": 850, "fuel_cost": 40000},
    {"from": "BOM", "to": "HYD", "distance": 600, "fuel_cost": 35000},
    {"from": "BLR", "to": "MAA", "distance": 300, "fuel_cost": 20000},
    {"from": "HYD", "to": "MAA", "distance": 500, "fuel_cost": 30000},
    {"from": "MAA", "to": "CCU", "distance": 1350, "fuel_cost": 60000},
]

# Insert into collection
collection.insert_many(airports_data)

print("Data inserted successfully into 'Kruskal_nodes' collection!")
