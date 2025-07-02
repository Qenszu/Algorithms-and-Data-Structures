def find_cycle(G):
    n = len(G)
    visited = [False for i in range(n)]
    times = [-1 for i in range(n)]
    Time = 0
    def DFS(v):
        nonlocal Time
        visited[v] = True
        times[v] = Time
        Time += 1
        for i in G[v]:
            if visited[i]:
                if times[v] - times[i] + 1 == 4:
                    return True
            else:
                if DFS(i):
                    return True
        Time -= 1
        return False
    
    for i in range(n):
        if visited[i] == False and DFS(i):
            return True
    return False

# 0 -- 1
# |  / |
# | /  |
# 3 -- 2
# times: 0 1 3 2
# nie wykrywa cyklu ponieważ DFS nie przechodzi nigdy po ścieżkach 0-3 i 1-2
G = [[1,3], [3,0,2], [1,3], [0,1,2]]
print(find_cycle(G))
#G = [[1],[0,2],[3,1],[]]