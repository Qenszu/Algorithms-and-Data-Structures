class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal(graph, n):
    edges = []
    for u in range(n):
        for v, weight in graph[u]:
            if u < v:  # Avoid adding edges twice
                edges.append((weight, u, v))
    
    edges.sort()
    
    ds = DisjointSet(n)
    mst = []
    total_weight = 0
    
    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == n - 1:
                break
    
    return mst, total_weight

def kruskal_edge_list(edges, n):
    edges.sort(key=lambda x: x[2])
    
    ds = DisjointSet(n)
    mst = []
    total_weight = 0
    
    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            if len(mst) == n - 1:
                break
    
    return mst, total_weight

if __name__ == "__main__":
    n = 6  # Number of vertices
    
    # Graph represented as adjacency list: [[(neighbor, weight)]]
    graph = [
        [(1, 4), (2, 3)],             # Vertex 0
        [(0, 4), (2, 5), (3, 9)],     # Vertex 1
        [(0, 3), (1, 5), (3, 7), (4, 4)], # Vertex 2
        [(1, 9), (2, 7), (4, 2), (5, 8)], # Vertex 3
        [(2, 4), (3, 2), (5, 1)],     # Vertex 4
        [(3, 8), (4, 1)]              # Vertex 5
    ]
    
    # Alternative edge list representation
    edge_list = [
        (0, 1, 4), (0, 2, 3),
        (1, 2, 5), (1, 3, 9),
        (2, 3, 7), (2, 4, 4),
        (3, 4, 2), (3, 5, 8),
        (4, 5, 1)
    ]

print(kruskal(graph, n))
    