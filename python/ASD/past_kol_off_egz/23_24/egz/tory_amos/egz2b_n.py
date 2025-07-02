from egz2btesty import runtests
from collections import deque

"""
Zlozonosc O(m) - gdzie m to ilosc koleji 
Moj algorytm wykorzystuje klasyczny algorytm BFS z opoznianiem wierzcholkow.
Tablica visited przechowuje dwa stany: czy dany wierzcholek v zostal juz odwiedzony 
danym typem torow
W kolejce wierzcholek v oznaczam jako odwiedzony dopiero gdy jego delay jest zerowy.
Podczas redukowania delay sprawdzamy czy dany wierzcholek v nie zostal juz odwiedzony danym typem torow 
i jezeli tak, algorytm nie przekazuje wierzcholka v z danym delay'em dalej do kolejki 
Jezli wierzcholek B zostal juz odwiedzony kazdym typem torow zwracam mniejszy wynik 
"""

def tory_amos( E, A, B ):
    maxi = 0

    for v, u, time, type in E:
        maxi = max(maxi, max(u, v))

    G = [[] for _ in range(maxi+1)]
    visited = [[False for _ in range(2)] for _ in range(maxi+1)]
    visited[A][0] = True
    visited[A][1] = True

    for v, u, time, type in E:
        if type == 'I':
            type = 0
        else:
            type = 1
        G[v].append((u, time, type))
        G[u].append((v, time, type))
    
    q = deque()
    q.append((0, A, 0, 1))
    mini = float("inf")

    while q:
        d, v, delay, t = q.popleft()

        if visited[B][0] and visited[B][1]:
            return mini

        if delay == 0 and not visited[v][t]:
            visited[v][t] = True

        if delay > 0:
            if not visited[v][t]:
                q.append((d+1, v, delay - 1, t))

        else:
            for u, time, type in G[v]:
                if v == A:
                    if not visited[u][type]:
                        q.append((d, u,  time, type))
                
                elif u == B:
                    if t == type == 0:
                        mini = min(mini, d + time + 5)
                    elif t == type == 1:
                        mini = min(mini, d + time + 10)
                    else:
                        mini = min(mini, d + time + 20)

                else:
                    if t == type == 0:
                        if not visited[u][type]:
                            q.append((d, u, time + 5, type))
                    elif t == type == 1:
                        if not visited[u][type]:
                            q.append((d, u, time + 10, type))
                    else:
                        if not visited[u][t]:
                            q.append((d, u, time + 20, type))


    return mini
  
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )

