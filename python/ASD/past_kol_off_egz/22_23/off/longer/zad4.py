from zad4testy import runtests
from collections import deque

'''
Algorytm szuka nakrotszej sciezki pomiedzy s do t zapamietujac ja
po czym przechodzac przez te najkrotsza sciezke po koleji usuwa kazda
krawedz i uruchamia bfs sprawdzajac czy sciezka ulegla wydluzeniu
Jezeli tak to zwracamy true
'''

def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje

    n = len(G)
    parent = [-1 for _ in range(n)]

    def bfs_parent(G, parent, n, s, t):
        visited = [False for _ in range(n)]
        visited[s] = True
        q = deque()
        q.append((s, 0))

        while q:
            v, time = q.popleft()

            if v == t:
                return time 

            for u in G[v]:
                if not visited[u]:
                    visited[u] = True
                    parent[u] = v
                    q.append((u, time + 1))

    min_path = bfs_parent(G, parent, n, s, t)

    def remove_edge(G, v, u):
        G[v].remove(u)
        G[u].remove(v)

    def add_edge(G, v, u):
        G[v].append(u)
        G[u].append(v)

    def bfs(G, n, s, t):
        visited = [False for _ in range(n)]
        visited[s] = True
        q = deque()
        q.append((s, 0))

        while q:
            v, time = q.popleft()

            if v == t:
                return time 

            for u in G[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append((u, time + 1))

    print(parent)
    x = parent[t]
    y = t

    while y != x and x != -1:
        remove_edge(G, x, y)
        new_path = bfs(G, n, s, t)

        if new_path is None:
            return (x, y)
        if new_path > min_path:
            return (x, y)
        else:
            add_edge(G, x, y)
            y = x
            x = parent[x]

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )

G = [[1, 2], [0, 2], [0, 1]]
s = 0
t = 2
#print(longer(G, s, t))