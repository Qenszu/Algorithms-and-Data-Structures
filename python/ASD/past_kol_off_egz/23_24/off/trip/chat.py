from zad9testy import runtests

# OPCJA 1: Topological Sort + DP (O(V+E))
from collections import deque

def trip_topological(M):
    m = len(M)
    n = len(M[0])
    
    G = [[] for _ in range(m*n)]
    in_degree = [0] * (m*n)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def coord_to_vertex(x, y):
        return x * n + y

    # Budowanie grafu
    for x in range(m):
        for y in range(n):
            current_vertex = coord_to_vertex(x, y)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:  
                    if M[x][y] < M[nx][ny]:  
                        neighbor_vertex = coord_to_vertex(nx, ny)
                        G[current_vertex].append(neighbor_vertex)
                        in_degree[neighbor_vertex] += 1

    # Topological sort + DP w jednym przejściu
    queue = deque()
    dp = [1] * (m*n)  # dp[i] = najdłuższa ścieżka kończąca się w i
    
    # Znajdź wszystkie wierzchołki bez wchodzących krawędzi
    for i in range(m*n):
        if in_degree[i] == 0:
            queue.append(i)
    
    max_path = 1
    
    while queue:
        v = queue.popleft()
        
        for u in G[v]:
            # Aktualizuj najdłuższą ścieżkę do u
            dp[u] = max(dp[u], dp[v] + 1)
            max_path = max(max_path, dp[u])
            
            # Zmniejsz stopień wejściowy
            in_degree[u] -= 1
            if in_degree[u] == 0:
                queue.append(u)
    
    return max_path

# OPCJA 2: DFS z memoizacją (może być szybsza w praktyce)
def trip_dfs_memo(M):
    m = len(M)
    n = len(M[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    memo = {}
    
    def dfs(x, y):
        if (x, y) in memo:
            return memo[(x, y)]
        
        max_length = 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and M[x][y] < M[nx][ny]:
                max_length = max(max_length, 1 + dfs(nx, ny))
        
        memo[(x, y)] = max_length
        return max_length
    
    result = 1
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))
    
    return result

# Wybierz jedną z funkcji jako główną
def trip(M):
    return trip_dfs_memo(M)  # lub trip_topological(M)


runtests(trip, all_tests=True)