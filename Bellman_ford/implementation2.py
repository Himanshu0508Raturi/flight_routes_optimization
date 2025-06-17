# app.py
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from data import airports, edges
from bellman_ford import bellman_ford, get_path
from graph_logic import build_graph, get_edge_labels
from layout_utils import get_custom_layout

st.set_page_config(
    page_title="Flight Route Optimizer",
    layout="wide",  # or "wide"
    initial_sidebar_state="collapsed"  # or "expanded" or "auto"
)
st.title("Flight Route Optimizer")
st.markdown("Major airports arranged in a polygon. Optimize route by Cost, Distance, or Time.")

# UI
source = st.selectbox("✈️ Select Source Airport", airports, index=0)
destination = st.selectbox("🛬 Select Destination Airport", airports, index=1)
criteria = st.radio("📊 Optimization Metric", ['Cost', 'Distance', 'Time'])

# Main Logic
G = build_graph(airports, edges)

if source and destination and criteria:
    dist, pred = bellman_ford(G, source, criteria)
    path = get_path(pred, destination)

    st.success(f"**Optimal Path ({criteria})**: {' → '.join(path)}")
    #st.info(f"**Total {criteria}**: {dist[destination]}")
    if(criteria == "Cost"):
        st.info(f"**Total {criteria}**: ₹{dist[destination]}")
    elif(criteria == "Distance"):
        st.info(f"**Total {criteria}**: {dist[destination]} KM")
    else:
        st.info(f"**Total {criteria}**: {dist[destination]} Hr")
    layout = get_custom_layout()
    edge_labels = get_edge_labels(G, criteria)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5))
    nx.draw_networkx_edges(G, layout, ax=ax, edge_color='gray', width=2)
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, layout, edgelist=path_edges, ax=ax, edge_color='red', width=3)
    nx.draw_networkx_nodes(G, layout, ax=ax, node_color='skyblue', node_size=1000, edgecolors='black')
    nx.draw_networkx_labels(G, layout, ax=ax, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, layout, edge_labels=edge_labels, ax=ax, font_size=7)

    ax.set_title(f"Flight Route Graph (Optimized by {criteria})", fontsize=14)
    ax.axis('off')
    st.pyplot(fig)
