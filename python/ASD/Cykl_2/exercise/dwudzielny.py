from collections import deque

class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the given number of vertices
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list representation
        self.colour = [-1] * vertices  # Colour array to store colours of vertices
        self.parent = [-1] * vertices  # Parent array for tracking BFS tree
    
    def add_edge(self, u, v):
        # Add an undirected edge between vertices u and v
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self):
        # Create a queue for BFS
        queue = deque()
        
        queue.append(0)  # Start BFS from vertex 0
        
        self.colour[0] = 0  # Assign the first colour (0) to the starting vertex
        
        while queue:
            # Dequeue a vertex from the queue
            vertex = queue.popleft()
            col = self.colour[vertex]  # Get the colour of the current vertex
            
            # Toggle the colour for the neighbors
            if col:
                col = 0
            else:
                col = 1
            
            for neighbor in self.graph[vertex]:

                if self.colour[neighbor] == -1:
                    # If the neighbor is not coloured, assign the toggled colour
                    queue.append(neighbor)
                    self.colour[neighbor] = col
                elif self.colour[neighbor] != col:
                    # If the neighbour has the same colour, the graph is not bipartite
                    return False                   
        
        return True
    
g = Graph(6)

# Add edges
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(0, 5)
g.add_edge(1, 4)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(1, 5)

# Check if the graph is bipartite
result = g.bfs()
print(result)

