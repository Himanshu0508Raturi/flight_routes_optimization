#app.py

import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from data import airports, edges, load_graph
from floyd_warshell import floyd_warshell, get_intermediate_path
from graph_logic import build_graph, get_edge_labels
from layout_util import get_custom_layout

st.set_page_config(
    page_title="Flight Route Optimizer",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Flight Route Optimizer")
st.markdown("Find the shortest or cheapest route between airports. Intermediate stopovers supported.")

# UI Elements
col1, col2 = st.columns(2)
with col1:
    source = st.selectbox("✈ Source Airport", airports, index=0)
    destination = st.selectbox("🛬 Destination Airport", airports, index=1)
with col2:
    criteria_display = st.radio("📊 Optimization Metric", ['Cost', 'Distance', 'Time'])
    criteria = criteria_display.lower()

# Intermediate Airports
intermediate_stops = st.multiselect(
    "🛑 Select Intermediate Airports (optional)",
    [a for a in airports if a not in [source, destination]]
)

# Graph Initialization
G = build_graph(airports, edges)

# Floyd-Warshall Precomputation
distances, predecessors = floyd_warshell(G, criteria)

if source and destination and source != destination:
    try:
        path, total = get_intermediate_path(
            G, source, destination, intermediate_stops,
            distances, predecessors, criteria
        )

        # Display Results
        st.success(f"*Optimal Path ({criteria.title()})*: {' → '.join(path)}")

        if criteria == "cost":
            st.info(f"💰 Total Cost: ₹{total}")
        elif criteria == "distance":
            st.info(f"📏 Total Distance: {total} KM")
        else:
            st.info(f"⏱ Total Time: {total} Hr")

        # Visualization
        layout = get_custom_layout()
        edge_labels = get_edge_labels(G, criteria)

        fig, ax = plt.subplots(figsize=(12, 8))
        nx.draw_networkx_edges(G, layout, ax=ax, edge_color='gray', width=1)

        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, layout, edgelist=path_edges, ax=ax,
                               edge_color='red', width=3, alpha=0.7)

        nx.draw_networkx_nodes(G, layout, ax=ax, node_color='skyblue',
                               node_size=1200, edgecolors='black')
        nx.draw_networkx_labels(G, layout, ax=ax, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, layout, edge_labels=edge_labels,
                                     ax=ax, font_size=8)

        ax.set_title("Optimized Flight Route", fontsize=14)
        ax.axis('off')
        st.pyplot(fig)

    except nx.NetworkXNoPath:
        st.error("❌ No path exists between the selected airports including the intermediate stops.")
