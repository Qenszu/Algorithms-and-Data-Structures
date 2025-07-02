from zad3testy import runtests
from collections import deque

'''
Algorytm szuka nakrotszej sciezki pomiedzy s do t zapamietujac ja
po czym przechodzac przez te najkrotsza sciezke po koleji usuwa kazda
krawedz i uruchamia bfs sprawdzajac czy sciezka ulegla wydluzeniu
Jezeli tak to zwracamy true
'''

def longer(G, s, t):
    # Najpierw sprawdzamy, czy istnieje jakakolwiek ścieżka z s do t
    parent, distance = bfs_shortest_path(G, s)
    if distance[t] == -1:  # t jest nieosiągalne z s
        return None
    
    original_distance = distance[t]
    
    # Znajdź wszystkie krawędzie na najkrótszej ścieżce (z s do t)
    edges_on_shortest_path = get_edges_on_shortest_path(G, parent, s, t)
    
    # Sprawdź każdą krawędź na najkrótszej ścieżce
    for u, v in edges_on_shortest_path:
        # Tymczasowo usuń krawędź {u, v}
        G[u].remove(v)
        G[v].remove(u)
        
        # Sprawdź, czy najkrótsza ścieżka się wydłużyła
        _, new_distance = bfs_shortest_path(G, s)
        
        # Przywróć krawędź
        G[u].append(v)
        G[v].append(u)
        
        if new_distance[t] > original_distance or new_distance[t] == -1:
            return (u, v) if u < v else (v, u)  # Zwracamy krawędź w kolejności rosnącej
    
    return None

def bfs_shortest_path(G, s):
    n = len(G)
    distance = [-1] * n
    parent = [-1] * n
    queue = deque([s])
    distance[s] = 0
    
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
    
    return parent, distance

def get_edges_on_shortest_path(G, parent, s, t):
    edges = set()
    v = t
    while v != s and v != -1:
        u = parent[v]
        edges.add((min(u, v), max(u, v)))  # Dodaj krawędź w kolejności rosnącej
        v = u
    return edges

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
