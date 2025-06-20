# data.py
import streamlit as st

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = st.secrets["MONGO_URI"]

client = MongoClient(MONGO_URI)
db = client["flightdb"]

# Fetch airport codes
airports = [doc["code"] for doc in db.airports.find({})]

# Fetch route edges
edges = []
for doc in db.routes.find({}):
    edge = (doc["source"], doc["dest"], {
        "Cost": doc["Cost"],
        "Distance": doc["Distance"],
        "Time": doc["Time"]
    })
    edges.append(edge)
