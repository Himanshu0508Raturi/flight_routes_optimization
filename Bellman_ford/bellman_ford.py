# bellman_ford.py

def bellman_ford(graph, source, weight):
    distance = {node: float('inf') for node in graph.nodes}
    predecessor = {node: None for node in graph.nodes}
    distance[source] = 0

    for _ in range(len(graph.nodes) - 1):
        for u, v, data in graph.edges(data=True):
            w = data[weight]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u
            if distance[v] + w < distance[u]:
                distance[u] = distance[v] + w
                predecessor[u] = v

    return distance, predecessor

def get_path(predecessor, destination):
    path = []
    while destination is not None:
        path.append(destination)
        destination = predecessor[destination]
    return path[::-1]
