from zad9testy import runtests

def maxflow( G,s ):
    # tu prosze wpisac wlasna implementacje
    n = 0

    for v, u, c in G:
        n = max(n, max(v, u))
    n += 1

    g = [[] for _ in range(n)]

    for v, u, c in G:
        g[v].append((u, c))

    for i in g:
        print(i)

    return 0

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( maxflow, all_tests = False )

G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)]  
s=2
print(maxflow(G, s))