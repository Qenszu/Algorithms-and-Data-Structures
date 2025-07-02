from zad4testy import runtests
from queue import PriorityQueue

"""
W algorytmie korzystam z zmodyfikowanego bfs w ktorym w kolejce przetrzymuje wysokosc maxymalna
i minimalna ktora przeliecial samolot i jezeli mozliwe jest dotarcie do wierzcholka y z
zachowaniem ze roznica miedzy pulapami jest mniejsza od 2*t to zwracam True
"""

def Flight(L,x,y,t):
    # tu prosze wpisac wlasna implementacje
    n = 0
    for v, u, p in L:
        n = max(n, max(v, u))
    n += 1

    G = [[] for _ in range(n)] 

    for v, u, p in L:
        G[v].append((u, p))
        G[u].append((v, p))

    noff = len(G[x])                    #number of first flight
    f = [[False for _ in range(noff)] for _ in range(n)]
    q = PriorityQueue()

    for i in range(noff):
        f[x][i] = True
        q.put((i, G[x][i][1], G[x][i][1], G[x][i][0]))

    while not q.empty():
        path, mini, maxi, v = q.get()

        if v == y:
            return True

        for u, d in G[v]:
            if not f[u][path]:
                if d < mini and maxi - d <= 2 * t:
                    f[u][path] = True
                    q.put((path, d, maxi, u))
                elif d > maxi and d - mini <= 2 * t:
                    f[u][path] = True
                    q.put((path, mini, d, u))
                elif d <= maxi and d >= mini:
                    f[u][path] = True
                    q.put((path, mini, maxi, u))

    return False

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
