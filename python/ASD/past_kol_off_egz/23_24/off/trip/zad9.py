from zad9testy import runtests
from queue import PriorityQueue

def trip(M):
    # tu prosze wpisac wlasna implementacje
    m = len(M)
    n = len(M[0])
    G = [[] for _ in range(m*n)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    v = 0

    for x in range(m):
        for y in range(n):
            M[x][y] = (v, M[x][y])
            v += 1


    for x in range(m):
        for y in range(n):  
            for dx, dy in direction:
                if x + dx > -1 and x + dx < m and y + dy > -1 and y + dy < n:
                    if M[x][y][1] < M[x+dx][y+dy][1]:
                        G[M[x][y][0]].append(M[x+dx][y+dy][0])

    q = PriorityQueue()
    maxi = 1
    
    for i in range(m * n):
        dist = [0 for _ in range(n * m)]
        dist[i] = 1
        q.put((1, i))


        while not q.empty():
            time, v = q.get()

            for u in G[v]:
                if dist[u] < dist[v] + 1:
                    dist[u] = dist[v] + 1
                    maxi = max(maxi, dist[u])
                    q.put((dist[u], u))


    return maxi
    

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )


M = [ [7,6,5,12],
[8,3,4,11],
[9,1,2,10] ]
#print(trip(M))