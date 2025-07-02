def kruskal(G):
    n = len(G)
    parent = [i for i in range(n)] 
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return False
    
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[x] += 1
        return True
    
    edges = []
    for u in range(n):
        for v, weight in G[u]:
            if u < v: 
                edges.append((weight, u, v))

    edges.sort()
    mst = []

    for weight, v, u in edges:
        if union(v, u):
            mst.append((v, u, weight))
            if len(mst) == n-1:
                break

    return mst

graph = [
        [(1, 4), (2, 3)],             # Vertex 0
        [(0, 4), (2, 5), (3, 9)],     # Vertex 1
        [(0, 3), (1, 5), (3, 7), (4, 4)], # Vertex 2
        [(1, 9), (2, 7), (4, 2), (5, 8)], # Vertex 3
        [(2, 4), (3, 2), (5, 1)],     # Vertex 4
        [(3, 8), (4, 1)]              # Vertex 5
    ]

print(kruskal(graph))

    
