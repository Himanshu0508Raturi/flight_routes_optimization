# graph_logic.py
import networkx as nx

def build_graph(nodes, edges):
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    for u, v, data in edges:
        G.add_edge(u, v, **data)
        # Add reverse edge if bidirectional
        G.add_edge(v, u, **data)  
    return G

def get_edge_labels(graph, criteria):
    return {(u, v): f"{data[criteria]}" for u, v, data in graph.edges(data=True)}