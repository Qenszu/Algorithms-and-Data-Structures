class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
        self.parent = [-1] * vertices
        self.visited = [False] * vertices
        self.taversal = []

    def add_edge(self, v, u):
        self.graph[v].append(u)

    def restart(self):
        for i in range(self.vertices):
            self.parent[i] = -1
            self.visited[i] = False
            self.traversal = []

    def DFS(self):
        self.restart()
        for vertex in range(self.vertices):
            if not self.visited[vertex]:
                self.dfs_visited(vertex)
        return self.taversal

    
    def dfs_visited(self, v):
        self.visited[v] = True
        self.taversal.append(v)

        for neighbor in self.graph[v]:
            if not self.visited[neighbor]:
                self.parent[neighbor] = v
                self.dfs_visited(neighbor)


g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

print(g.DFS())