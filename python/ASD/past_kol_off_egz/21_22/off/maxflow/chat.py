from zad9testy import runtests

from collections import deque, defaultdict
from copy import deepcopy

def build_graph(G):
    graph = defaultdict(dict)
    for u, v, c in G:
        graph[u][v] = c
        if u not in graph[v]:
            graph[v][u] = 0
    return graph

def bfs(graph, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in visited and graph[u][v] > 0:
                visited.add(v)
                parent[v] = u
                if v == t:
                    return True
                queue.append(v)
    return False

def edmonds_karp(graph, s, t):
    flow = 0
    while True:
        parent = {}
        if not bfs(graph, s, t, parent):
            break
        # znajdź przepustowość ścieżki
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = u
        # aktualizuj przepływ
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        flow += path_flow
    return flow

def maxflow(G, s):
    n = max(max(u, v) for u, v, _ in G) + 1
    max_total = 0

    for i in range(n):
        for j in range(i + 1, n):
            if i == s or j == s:
                continue
            graph1 = build_graph(G)
            flow1 = edmonds_karp(graph1, s, i)
            graph2 = deepcopy(graph1)
            flow2 = edmonds_karp(graph2, s, j)
            total = flow1 + flow2
            if total > max_total:
                max_total = total
    return max_total


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )