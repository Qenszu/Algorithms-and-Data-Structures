from kol3btesty import runtests
from queue import PriorityQueue

def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    cost = [float("inf") for _ in range(n+1)]
    cost[s] = 0
    q = PriorityQueue()
    q.put((0, s))
    G.append([])

    for i in range(n):
        G[i].append((n, A[i]))
        G[n].append((i, A[i]))
    

    while not q.empty():
        p, v = q.get()

        for u, c in G[v]:
            if cost[u] > cost[v] + c:
                cost[u] = cost[v] + c
                q.put((cost[u], u))
    
    return cost[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )