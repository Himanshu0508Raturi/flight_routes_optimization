# graph_logic.py

import networkx as nx

def build_graph(nodes, edges):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def get_edge_labels(graph, criteria):
    if criteria == "Cost":
        return {(u, v): f"₹{data['Cost']}" for u, v, data in graph.edges(data=True)}
    elif criteria == "Distance":
        return {(u, v): f"{data['Distance']} km" for u, v, data in graph.edges(data=True)}
    elif criteria == "Time":
        return {(u, v): f"{data['Time']} hr" for u, v, data in graph.edges(data=True)}
