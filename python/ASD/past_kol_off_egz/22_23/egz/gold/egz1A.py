from egz1Atesty import runtests
from queue import PriorityQueue

def gold(G,V,s,t,r):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    
    dist = [[float("inf") for i in range(2)] for _ in range(n)]
    dist[s][0] = 0
    dist[s][1] = -V[s]

    q = PriorityQueue()
    q.put((0, s, 0))
    q.put((-V[s], s, 1))

    while not q.empty():
        d, v, rob = q.get()
        
        if rob:
            for u, cost in G[v]:
                if dist[u][rob] > dist[v][rob] + cost*2 + r:
                    dist[u][rob] = dist[v][rob] + cost*2 + r
                    q.put((dist[u][rob], u, 1))
        else:
            for u, cost in G[v]:
                if dist[u][rob] > dist[v][rob] + cost:
                    dist[u][rob] = dist[v][rob] + cost
                    q.put((dist[u][rob], u, 0))
                if dist[u][1] > dist[v][rob] + cost*2 + r - V[v]:
                    dist[u][1] = dist[v][rob] + cost*2 + r - V[v]
                    q.put((dist[u][1], u, 1))
    for i in range(n):
        dist[i][0] -= V[i]
        
    return min(dist[t])

G = [[(1,9), (2,2)],                # 0
    [(0,9), (3,2), (4,6)],          # 1
    [(0,2), (3,7), (5,1)],          # 2
    [(1,2), (2,7), (4,2), (5,3)],   # 3
    [(1,6), (3,2), (6,1)],          # 4
    [(2,1), (3,3), (6,8)],          # 5
    [(4,1), (5,8)] ]                # 6
V = [25,30,20,15,5,10,0]
s = 1
t = 2 
r = 7

#gold(G, V, s, t, r)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )