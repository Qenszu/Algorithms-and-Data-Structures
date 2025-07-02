from egz3atesty import runtests
from queue import PriorityQueue

"""
Zlozonosc: O(nlogn)
Algoryt wykorzystuje zmodyfikowanego BFS ktory na poczatku do kolejki prioretytowej 
wrzuca po koleji grzyby o najmniejszym indeksie, po czym uruchamia BFS ktory odpowiednio
wyciag z kolejki grzyba z najnizszym czasem (w razie remisu wyciagany jest pierwsze ten o 
mniejszym indeksie) i "opanowywuje" swoich sasiadow
"""

def mykoryza( G,T,d ):
    n = len(G)
    occ = [-1 for _ in range(n)]
    q = PriorityQueue()
    cnt = 1
    i = 0
    for m in T:
        occ[m] = m
        q.put((0, i, m))
        i += 1

    while not q.empty():
        time, m, tree = q.get()

        for u in G[tree]:
            if occ[u] == -1:
                occ[u] = m
                q.put((time+1, m, u))
                if m == d:
                    cnt += 1

    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )