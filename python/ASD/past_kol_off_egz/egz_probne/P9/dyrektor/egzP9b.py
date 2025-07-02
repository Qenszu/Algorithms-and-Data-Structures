from egzP9btesty import runtests
from collections import defaultdict

def dyrektor(G, R):
    from collections import deque

    n = len(G)
    graph = [deque() for _ in range(n)]

    # Skopiuj G do graph, odejmując tylko tyle krawędzi ile podano w R (ważne dla multigrafu!)
    for u in range(n):
        available = G[u][:]
        to_remove = R[u]
        for rem in to_remove:
            available.remove(rem)  # usuń tylko jedną wystąpienie
        graph[u] = deque(available)

    # Hierholzer's algorithm
    path = []
    stack = [0]

    while stack:
        v = stack[-1]
        if graph[v]:
            stack.append(graph[v].popleft())
        else:
            path.append(stack.pop())

    return path[::-1]  # odwrócenie daje właściwą kolejność

runtests(dyrektor, all_tests=True)
