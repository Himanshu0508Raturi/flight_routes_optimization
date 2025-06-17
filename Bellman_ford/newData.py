from pymongo import MongoClient

# Replace with your actual MongoDB URI
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Access your MongoDB URI
MONGO_URI = os.getenv("MONGODB_URI")

# Example: use it with pymongo
client = MongoClient(MONGO_URI)
db = client["flightdb"]

# Create or select collection
collection = db["newnode"]

# Full airport data
airports_data = [
    {"code": "DEL", "name": "Indira Gandhi International Airport", "lat": 28.5562, "lon": 77.1000},
    {"code": "BOM", "name": "Chhatrapati Shivaji Maharaj International Airport", "lat": 19.0896, "lon": 72.8656},
    {"code": "BLR", "name": "Kempegowda International Airport", "lat": 13.1986, "lon": 77.7066},
    {"code": "MAA", "name": "Chennai International Airport", "lat": 12.9941, "lon": 80.1709},
    {"code": "HYD", "name": "Rajiv Gandhi International Airport", "lat": 17.2403, "lon": 78.4294},
    {"code": "CCU", "name": "Netaji Subhas Chandra Bose International Airport", "lat": 22.6540, "lon": 88.4467},
    {"code": "AMD", "name": "Sardar Vallabhbhai Patel International Airport", "lat": 23.0732, "lon": 72.6347},
    {"code": "GOI", "name": "Goa International Airport", "lat": 15.3800, "lon": 73.8312},
    {"code": "PAT", "name": "Jay Prakash Narayan Airport", "lat": 25.5913, "lon": 85.0870},
    {"code": "PNQ", "name": "Pune International Airport", "lat": 18.5799, "lon": 73.9120},
    {"code": "TRV", "name": "Trivandrum International Airport", "lat": 8.4821, "lon": 76.9201},
    {"code": "STV", "name": "Surat International Airport", "lat": 21.1141, "lon": 72.7411},
    {"code": "VGA", "name": "Vijayawada International Airport", "lat": 16.5304, "lon": 80.7969},
    {"code": "IXC", "name": "Chandigarh International Airport", "lat": 30.6735, "lon": 76.7885},
    {"code": "JAI", "name": "Jaipur International Airport", "lat": 26.8242, "lon": 75.8122}
]

# Insert into collection
collection.insert_many(airports_data)

print("Data inserted successfully into 'newnode' collection!")
