from zad8testy import runtests
from collections import deque
import heapq

def sum_of_oil(T, v, u):
    n = len(T)
    m = len(T[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((v, u))
    result = T[v][u]
    T[v][u] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if -1 < nx < n and -1 < ny < m:
                if T[nx][ny] != 0:
                    result += T[nx][ny]
                    T[nx][ny] = 0
                    q.append((nx, ny))

    return result

    

def plan(T):
    # tu prosze wpisac wlasna implementacje
    heap = []
    m = len(T[0])
    T[0][0] = sum_of_oil(T, 0, 0)
    oil = T[0][0] - 1
    stops = 1

    for i in range(1, m):
        if i == m - 1:
            return stops
        if T[0][i] != 0:
            heapq.heappush(heap, -sum_of_oil(T, 0, i))
        if oil == 0:
            stops += 1
            oil += -heapq.heappop(heap)
        oil -= 1

    return stops



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

