def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for i in dist:
        print(i)

    return dist

def floyd_warshall_with_path(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    next_node = [[-1 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                next_node[i][j] = j
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]
    
    return dist, next_node

def reconstruct_path(next_node, u, v):
    if next_node[u][v] == -1:
        return []
    
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    
    return path


INF = float("inf")

graph = [
    [0,   3,  INF, 7],
    [8,   0,  2,   INF],
    [5,   INF, 0,  1],
    [2,   INF, INF, 0]
]

print(floyd_warshall(graph))