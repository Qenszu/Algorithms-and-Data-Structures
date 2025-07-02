""""Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
wymiarach NxN ruchem skoczka szachowego"""

N = 5
T = [[0 for h in range(N)] for _ in range(N)]

def wypelnij(T, N, x = 0, y = 0, r = 1):
    T[x][y] = r
    ruchy = [(1, 2), (-2, -1), (-1, -2), (2, 1), (-2, 1), (-1, 2), (2, -1), (1, -2)]
    
    if r == N*N:
        return True
    
    for dx, dy in ruchy:
        if x + dx > -1 and x + dx < N and y + dy > -1 and y + dy < N:
            if T[x+dx][y+dy] == 0:
                if wypelnij(T, N, x+dx, y+dy, r+1):
                    return True
                else:
                    T[x+dx][y+dy] = 0


wypelnij(T, N)

for i in range(len(T)):
    print(T[i])

     
    



