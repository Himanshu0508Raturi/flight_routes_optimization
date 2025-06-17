import networkx as nx

def floyd_warshell(graph, criteria):
    nodes = list(graph.nodes())
    n = len(nodes)
    node_index = {node: i for i, node in enumerate(nodes)}

    dist = [[float('inf')] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, data in graph.edges(data=True):
        i = node_index[u]
        j = node_index[v]
        dist[i][j] = data[criteria]
        pred[i][j] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    dist_dict = {
        u: {v: dist[node_index[u]][node_index[v]] for v in nodes} for u in nodes
    }
    pred_dict = {
        u: {v: pred[node_index[u]][node_index[v]] for v in nodes} for u in nodes
    }

    return dist_dict, pred_dict


def get_intermediate_path(graph, source, dest, intermediates, dist, pred, criteria):
    path = [source]
    total = 0
    current = source

    for intermediate in intermediates:
        if intermediate not in pred[current] or pred[current][intermediate] is None:
            raise nx.NetworkXNoPath()

        segment = []
        node = intermediate
        while node != current:
            segment.append(node)
            node = pred[current][node]
            if node is None:
                raise nx.NetworkXNoPath()

        path += segment[::-1]
        total += dist[current][intermediate]
        current = intermediate

    # Add final destination
    segment = []
    node = dest
    while node != current:
        segment.append(node)
        node = pred[current][node]
        if node is None:
            raise nx.NetworkXNoPath()

    path += segment[::-1]
    total += dist[current][dest]

    return path, total


def get_path(graph, source, dest, dist, pred):
    path = []
    current = dest
    while current != source:
        path.append(current)
        current = pred[source][current]
        if current is None:
            raise nx.NetworkXNoPath()
    path.append(source)
    path.reverse()
    return path, dist[source][dest]
