from graph import *

g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 5)
g.add_edge(3, 4)
g.add_edge(4, 6)

    
def dfs(G, start_vertex):
    # Mark all vertices as not visited
    visited = [False] * G.vertices
        
    # List to store DFS traversal order
    traversal = []
        
    # Call the recursive helper function
    _dfs_recursive(G, start_vertex, visited, traversal)
        
    return visited
    
def _dfs_recursive(G, vertex, visited, traversal):
    # Mark the current node as visited and add to traversal
    visited[vertex] = True
    traversal.append(vertex)
        
    # Recur for all adjacent vertices
    for neighbor in G.graph[vertex]:
        if not visited[neighbor]:
            _dfs_recursive(G, neighbor, visited, traversal)
    
# Iterative DFS version using a stack
def dfs_iterative(G, start_vertex):
    # Mark all vertices as not visited
    visited = [False] * G.vertices
        
    # Create a stack for DFS
    stack = []
        
    # Push the start vertex
    stack.append(start_vertex)
        
    # List to store DFS traversal order
    traversal = []
        
    while stack:
        # Pop a vertex from stack
        vertex = stack.pop()
            
        # If not visited, mark it as visited and add to traversal
        if not visited[vertex]:
            visited[vertex] = True
            traversal.append(vertex)
            
        # Get all adjacent vertices
        # Push all unvisited neighbors to stack
        for neighbor in reversed(G.graph[vertex]):  # Reversed to maintain similar order to recursive
            if not visited[neighbor]:
                stack.append(neighbor)
        
    return traversal

print(dfs(g, 2))