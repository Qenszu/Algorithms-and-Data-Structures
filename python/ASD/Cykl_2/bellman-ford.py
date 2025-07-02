def bellman_ford(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    predecessor = [None] * n
    dist[source] = 0
    
    edges = []
    for u in range(n):
        for v, weight in graph[u]:
            edges.append((u, v, weight))
    
    for _ in range(n - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                predecessor[v] = u
    
    negative_cycle = False
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            negative_cycle = True
            break
    
    return dist, predecessor, negative_cycle

def reconstruct_path(predecessor, source, destination):
    if destination == source:
        return [source]
    
    if predecessor[destination] is None:
        return []
    
    path = reconstruct_path(predecessor, source, predecessor[destination])
    path.append(destination)
    return path