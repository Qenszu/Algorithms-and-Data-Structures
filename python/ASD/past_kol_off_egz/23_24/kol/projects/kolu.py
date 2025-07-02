from kolutesty import runtests
from collections import deque

"""
Algorytm tworzy odpowiedni graf jako jednokierunkowa liste sasiedztwa gdzie
krawedz prowadzi od v do u jezeli aby wykonac zadanie v najpierw musimy wykonac zadanie u
po czym zmotyfikowany bfs wylicza ile jednostek czasu jest potrzebne by wykonac 
wszystkie zadania
"""

def projects(n, L):
    if n <= 0:
        return 0
    
    graph = [[] for _ in range(n)]
    in_degree = [0] * n
    
    for p, q in L:
        graph[q].append(p)
        in_degree[p] += 1
    
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    time_units = 0
    processed = 0
    
    while queue:
        level_size = len(queue)
        time_units += 1
        
        for _ in range(level_size):
            current = queue.popleft()
            processed += 1
            
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    
    if processed != n:
        return -1
    
    return time_units

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True)
