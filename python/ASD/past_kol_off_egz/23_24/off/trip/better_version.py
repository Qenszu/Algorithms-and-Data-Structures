from zad9testy import runtests
from collections import deque

def trip(M):
    m = len(M)
    n = len(M[0])
    
    G = [[] for _ in range(m*n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    

    def coord_to_vertex(x, y):
        return x * n + y

    for x in range(m):
        for y in range(n):
            current_vertex = coord_to_vertex(x, y)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:  
                    if M[x][y] < M[nx][ny]:  
                        neighbor_vertex = coord_to_vertex(nx, ny)
                        G[current_vertex].append(neighbor_vertex)

    time = [1 for _ in range(m*n)]


    def bfs(G, s, time):
        q = deque()
        q.append((1, s))
        visited = [0 for _ in range(m*n)]
        visited[s] = 1
        maxi = 1

        while q:
            t, v = q.pop()
            maxi = max(maxi, t)

            for u in G[v]:
                if time[u] != 1:
                    time[s] = max(time[s], t + time[u])
                else:
                    if visited[u] < visited[v] + 1:
                        visited[u] = visited[v] + 1
                        q.append((visited[u], u))
        
        time[s] = max(time[s], maxi)

    for i in range(m):
        for j in range(n):
            ind = coord_to_vertex(i, j)
            if time[ind] == 1:
                bfs(G, ind, time)

    return max(time)





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(trip, all_tests=True)
