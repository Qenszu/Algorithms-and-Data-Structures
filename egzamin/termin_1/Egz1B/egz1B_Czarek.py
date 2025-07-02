from egz1Btesty import runtests
from queue import Queue
from math import inf

"""
Cezary Szczepanek
O(EV + E^2)
Dla kazdego wierzchołka zliczamy z rodziców, a następnie sprawdzamy dla kazdej krawędzi (a -> b)
czy parent count wierzcholka b jest równy 1, jesli tak to po usunieciu krawedzi nie da sie juz do niego dotrzeć.
"""



def construct_graph(V,E):
    graph = [[] for _ in range(V)]
    for a,b in E:
        graph[a].append(b)
    return graph


def critical(V, E):
    graph = construct_graph(V, E)
    counter = 0

    for a in range(V):
        visited = [False] * V
        parent_count = [0] * V

        def dfs(v):
            visited[v] = True
            for u in graph[v]:
                if not visited[u]:
                    parent_count[u] += 1
                    dfs(u)
                else:
                    parent_count[u] += 1

        dfs(a)

        for b in graph[a]:
            if visited[b] and parent_count[b] == 1:
                counter += 1

    return counter

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = True)