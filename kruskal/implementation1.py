import streamlit as st
import folium
from streamlit_folium import st_folium

airports = {
    "DEL": {"name": "Indira Gandhi", "city": "Delhi", "lat": 28.5562, "lon": 77.1000},
    "BOM": {"name": "Chhatrapati Shivaji", "city": "Mumbai", "lat": 19.0896, "lon": 72.8656},
    "BLR": {"name": "Kempegowda", "city": "Bangalore", "lat": 13.1986, "lon": 77.7066},
    "MAA": {"name": "Chennai", "city": "Chennai", "lat": 12.9941, "lon": 80.1707},
    "HYD": {"name": "Rajiv Gandhi", "city": "Hyderabad", "lat": 17.2403, "lon": 78.4294},
    "CCU": {"name": "Netaji Subhas", "city": "Kolkata", "lat": 22.6547, "lon": 88.4467},
}

flights = [
    {"from": "DEL", "to": "BOM", "distance": 1150, "fuel_cost": 50000},
    {"from": "DEL", "to": "BLR", "distance": 1750, "fuel_cost": 75000},
    {"from": "DEL", "to": "HYD", "distance": 1250, "fuel_cost": 55000},
    {"from": "BOM", "to": "BLR", "distance": 850, "fuel_cost": 40000},
    {"from": "BOM", "to": "HYD", "distance": 600, "fuel_cost": 35000},
    {"from": "BLR", "to": "MAA", "distance": 300, "fuel_cost": 20000},
    {"from": "HYD", "to": "MAA", "distance": 500, "fuel_cost": 30000},
    {"from": "MAA", "to": "CCU", "distance": 1350, "fuel_cost": 60000},
]

class KruskalsAlgorithm:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = sorted(edges, key=lambda x: x['weight'])
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1
    
    def run(self):
        mst = []
        for edge in self.edges:
            if self.find(edge['from']) != self.find(edge['to']):
                self.union(edge['from'], edge['to'])
                mst.append(edge)
            if len(mst) == len(self.vertices) - 1:
                break
        return mst

st.title(" Indian Flight Route Optimization")
st.markdown("Manual implementation of Kruskal's Algorithm for flight optimization")

weight_type = st.radio("Optimize by:", ["distance", "fuel_cost"], index=0)

edges = [{
    'from': f['from'],
    'to': f['to'],
    'weight': f[weight_type],
    'distance': f['distance'],
    'fuel_cost': f['fuel_cost']
} for f in flights]

kruskal = KruskalsAlgorithm(vertices=list(airports.keys()), edges=edges)
mst_edges = kruskal.run()

original_cost = sum(f[weight_type] for f in flights)
optimized_cost = sum(e[weight_type] for e in mst_edges)
savings = original_cost - optimized_cost

st.subheader("Optimal Flight Routes (Minimum Spanning Tree)")
st.table({
    "From": [e['from'] for e in mst_edges],
    "To": [e['to'] for e in mst_edges],
    "Distance (km)": [e['distance'] for e in mst_edges],
    "Fuel Cost (₹)": [f"₹{e['fuel_cost']:,}" for e in mst_edges],
    "Selected Weight": [e['weight'] for e in mst_edges]
})

st.success(f"Total Savings: ₹{savings:,} ({savings/original_cost*100:.2f}% reduction)")

st.subheader("Flight Network Visualization")

map_center = [sum(airport['lat'] for airport in airports.values()) / len(airports),
              sum(airport['lon'] for airport in airports.values()) / len(airports)]
m = folium.Map(location=map_center, zoom_start=5)

for code, data in airports.items():
    folium.Marker([data['lat'], data['lon']], popup=f"{code}: {data['name']}", icon=folium.Icon(color="blue")).add_to(m)

for flight in flights:
    from_airport = airports[flight['from']]
    to_airport = airports[flight['to']]
    folium.PolyLine(
        locations=[[from_airport['lat'], from_airport['lon']], [to_airport['lat'], to_airport['lon']]],
        color="darkcyan",
        weight=1,
        opacity=0.6
    ).add_to(m)

for edge in mst_edges:
    from_airport = airports[edge['from']]
    to_airport = airports[edge['to']]
    folium.PolyLine(
        locations=[[from_airport['lat'], from_airport['lon']], [to_airport['lat'], to_airport['lon']]],
        color="red",
        weight=3,
        tooltip=f"{edge['from']}-{edge['to']}: {edge[weight_type]}"
    ).add_to(m)

st_folium(m)

st.subheader("✈ Flight Disruption Simulation")
if mst_edges:
    disabled_flight = st.selectbox("Select a flight to cancel:", [f"{e['from']}-{e['to']}" for e in mst_edges])
    
    if st.button("Re-optimize Network"):
        remaining_flights = [f for f in flights if not (f['from'] == disabled_flight.split('-')[0] and f['to'] == disabled_flight.split('-')[1])]
        
        new_edges = [{
            'from': f['from'],
            'to': f['to'],
            'weight': f[weight_type],
            'distance': f['distance'],
            'fuel_cost': f['fuel_cost']
        } for f in remaining_flights]
        
        kruskal = KruskalsAlgorithm(vertices=list(airports.keys()), edges=new_edges)
        new_mst = kruskal.run()
        
        st.success("New Optimal Routes After Disruption")
        st.table({
            "From": [e['from'] for e in new_mst],
            "To": [e['to'] for e in new_mst],
            "Distance (km)": [e['distance'] for e in new_mst],
            "Fuel Cost (₹)": [f"₹{e['fuel_cost']:,}" for e in new_mst]
        })

