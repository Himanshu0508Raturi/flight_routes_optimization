# data.py
import networkx as nx
from pymongo import MongoClient
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
MONGO_URI = st.secrets["MONGO_URI"]
client = MongoClient(MONGO_URI)
db = client["flightdb"]

# Fetch airport codes
airports = [doc["code"] for doc in db.airports.find({})]

# Fetch route edges
edges = []
for doc in db.edges.find({}):
    edge = (doc["source"], doc["destination"], {
        "cost": doc["cost"],
        "distance": doc["distance"],
        "time": doc["time"]
    })
    edges.append(edge)




def load_graph():
    G = nx.DiGraph()
    for airport in airports:
        G.add_node(airport)
    for u, v, attr in edges:
        G.add_edge(u, v, **attr)
    return G
