"""
1. G -> nieskierowany ,  z wagami ze zbioru (1, |E|),  x, y zadane wierzcholki 

2. Sciezka Hamiltona w DAG

3. Dobry początek: G -> skierowany, czy dojde do kazdego 

4. Znaleźć cykl Eulera (macierz)

6. Dwie kliki G->nieskierowany

"""

def dfs(G, start_vertex):
    # Mark all vertices as not visited
    visited = [False] * len(G) 
        
        
    # Call the recursive helper function
    _dfs_recursive(G, start_vertex, visited)
        
    return visited

def find_klika(G, vertex, visited, neighbor):
    visited[vertex] = True

    for n in neighbor:
        pass

    
def _dfs_recursive(G, vertex, visited):
    # Mark the current node as visited and add to traversal
    visited[vertex] = True
        
    # Recur for all adjacent vertices
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            _dfs_recursive(G, neighbor, visited)



