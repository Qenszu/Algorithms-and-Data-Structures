class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, v, u):
        self.graph[v].append(u)

    def print_graph(self):
        for i in range(self.vertices):
            print(i, end=": ")
            for j in self.graph[i]:
                print(j, end="  ")
            print()
            
            
    