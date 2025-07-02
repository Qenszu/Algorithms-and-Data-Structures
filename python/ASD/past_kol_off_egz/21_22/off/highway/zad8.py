from zad8testy import runtests
from math import sqrt, ceil

def distance(a, b):
    return ceil(sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))

def highway(A):#wersja 5 razy szybsza :(
    n = len(A)
    if n < 2: return 0
    
    # Generowanie i sortowanie krawędzi - O(n² log n)
    edges = []
    for i in range(n-1):
        for j in range(i+1, n):
            edges.append((distance(A[i], A[j]), i, j))
    edges.sort()
    
    min_diff = float('inf')
    
    # Sliding window - O(n² α(n))
    left = 0
    while left <= len(edges) - (n-1):
        parent = list(range(n))
        rank = [0]*n
        
        # Zoptymalizowana funkcja find
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # Podwójne spłaszczenie
                u = parent[u]
            return u
        
        components = n  # Liczba niepołączonych komponentów
        right = left
        current_max = 0  # Maksymalna waga w aktualnym oknie
        
        while components > 1 and right < len(edges):
            d, u, v = edges[right]
            root_u = find(u)
            root_v = find(v)
            
            if root_u != root_v:
                # Union by rank
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_u] = root_v
                    if rank[root_u] == rank[root_v]:
                        rank[root_v] += 1
                components -= 1
                current_max = d
                
                if components == 1:  # Wszystkie miasta połączone
                    current_diff = current_max - edges[left][0]
                    if current_diff < min_diff:
                        min_diff = current_diff
                    break  # Możemy przerwać wewnętrzną pętlę
            right += 1
        
        left += 1  # Przesuwamy lewą granicę okna
    
    return min_diff if min_diff != float('inf') else 0

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )