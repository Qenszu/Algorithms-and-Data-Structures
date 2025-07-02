def dfs(G):
    traversal = []
        
        
    # Call the recursive helper function
    start = 0
    def _dfs_recursive(G, vertex):
        traversal.append(vertex)
        nonlocal start
    # Mark the current node as visited and add to traversal
        
    # Recur for all adjacent vertices
        x = vertex
        for i in range(len(G)):
            if G[vertex][i]:
                G[vertex][i] = 0
                G[i][vertex] = 0
                x = i
                break
        if x != vertex:
            start = x
            _dfs_recursive(G, x)

    _dfs_recursive(G, 0)
    flag = True
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == 1:
                flag = False
                break
    
        
    if flag and start == 0:
        return traversal[:-1]
    return ["N", "I", "M", "A"]
    

    




G = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

print(dfs(G))