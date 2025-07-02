from zad8testy import runtests
from math import sqrt, ceil

def distance(a, b):
    return ceil(sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2))

def highway(A):#wersja 5 razy szybsza :(
    n = len(A)
    if n < 2: return 0

    edges = []

    for i in range(n-1):
        for j in range(i+1, n):
            edges.append((distance(A[i], A[j]), i, j))
    edges.sort()

    min_diff = float("inf")
    left = 0

    while left <= len(edges) - (n-1):
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]  # path compression (skok o dwa poziomy)
                u = parent[u]
            return u
        
        city_connect = 1
        right = left
        crr_max = 0

        while city_connect < n and right < len(edges):
            d, v, u = edges[right]

            v = find(v)
            u = find(u)

            if v != u:
                if rank[v] > rank[u]:
                    parent[u] = v
                else:
                    parent[v] = u
                    if rank[v] == rank[u]:
                        rank[v] += 1
                city_connect += 1
                crr_max = d

                if city_connect == n:
                    curr_diff = crr_max - edges[left][0]
                    if curr_diff < min_diff:
                        min_diff = curr_diff
                    break
            right += 1
        left += 1

    return min_diff 
    
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )