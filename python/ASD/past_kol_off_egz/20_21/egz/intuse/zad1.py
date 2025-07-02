from zad1testy import runtests
from queue import Queue


def intuse( I, x, y ):
    """tu prosze wpisac wlasna implementacje"""

    n = len(I)
    G = [[] for _ in range(n+2)]
    T = [False] * (n+2)

    for i in range(n):
        for j in range(n):
            if I[i][1] == I[j][0]:
                G[i].append(j)
        if I[i][0] == x:
            G[n].append(i)
        if I[i][1] == y:
            G[i].append(n+1)

    #for i in G:
        #print(i)
    
    def dfs(G, v, n):
        if T[v]:
            return True
        for u in G[v]:
            if u == n+1:
                T[v] = True
                return True
            elif dfs(G, u, n):
                T[v] = True
                return True
        return False

    for i in G[n]:
        T[i] = dfs(G, i, n)

    
    res = []

    for i in range(n):
        if T[i]:
            res.append(i)
         

    sorted(res)

    return res

    
runtests( intuse )
#I = [ (3,4), (2,5), (1,3), (4,6), (1,4), (1, 2)]
#print(intuse(I, 1, 6))
