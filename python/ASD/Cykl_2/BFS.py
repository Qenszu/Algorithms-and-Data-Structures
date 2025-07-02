from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start_vertex):
        # Mark all vertices as not visited
        visited = [False] * self.vertices
        
        # Create a queue for BFS
        queue = deque()
        
        # Mark the start vertex as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)
        
        # List to store BFS traversal order
        traversal = []
        
        while queue:
            # Dequeue a vertex from queue and print it
            vertex = queue.popleft()
            traversal.append(vertex)
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it
            # visited and enqueue it
            for neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return traversal
    
# Create a graph with 6 vertices
g = Graph(6)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)

# Perform BFS starting from vertex 0
result = g.bfs(0, 5)
print("BFS traversal starting from vertex 0:")
print(result)  # Output will be: [0, 1, 2, 3, 4, 5]

