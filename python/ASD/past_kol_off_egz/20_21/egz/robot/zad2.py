from zad2testy import runtests
from queue import PriorityQueue

def direction(dir):
    if dir == (0, 1):
        return 0
    if dir == (0, -1):
        return 1
    if dir == (1, 0):
        return 2
    return 3

def robot( L, A, B ):
    """tu prosze wpisac wlasna implementacje"""
    w = len(L)
    k = len(L[0])

    dist = [[[float("inf") for _ in range(4)] for _ in range(k)] for _ in range(w)]
    dist[A[1]][A[0]][0] = 0
    q = PriorityQueue()
    q.put((0, A[1], A[0], (0, 1), 0))
    time = [60, 40, 30]

    while not q.empty():
        d, x, y, dire, step = q.get()
        dx, dy = dire
        if step > 2:
            step = 2
        if  L[x+dx][y+dy] != 'X':
            if dist[x+dx][y+dy][direction(dire)] > dist[x][y][direction(dire)] + time[step]:
                dist[x+dx][y+dy][direction(dire)] = dist[x][y][direction(dire)] + time[step]
                q.put((dist[x+dx][y+dy][direction(dire)], x + dx, y + dy, dire, step + 1)) 
        
        if  L[x+dy][y+dx] != 'X':
            if dist[x+dy][y+dx][direction((dy, dx))] > dist[x][y][direction(dire)] + 45 + time[0]:
                dist[x+dy][y+dx][direction((dy, dx))] = dist[x][y][direction(dire)] + 45 + time[0]
                q.put((dist[x+dy][y+dx][direction((dy, dx))], x + dy, y + dx, (dy, dx), 1))
        
        if  L[x-dy][y-dx] != 'X':
            if dist[x-dy][y-dx][direction((-dy, -dx))] > dist[x][y][direction(dire)] + 45 + time[0]:
                dist[x-dy][y-dx][direction((-dy, -dx))] = dist[x][y][direction(dire)] + 45 + time[0]
                q.put((dist[x-dy][y-dx][direction((-dy, -dx))], x - dy, y - dx, (-dy, -dx), 1))

    x = min(dist[B[1]][B[0]])

    return x if x != float("inf") else None

    
runtests( robot )


