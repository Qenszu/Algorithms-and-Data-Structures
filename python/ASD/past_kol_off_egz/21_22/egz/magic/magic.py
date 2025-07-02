from egz2btesty import runtests

def magic( C ):
    n = len(C)
    f = [-1 for _ in range(n)]
    f[0] = 0

    for i in range(n):
        for j in range(1, 4):
            if C[i][j][1] != -1 and C[i][j][1] > i and f[i] != -1:
                if C[i][0] - C[i][j][0] < 11:                           #w skrzyni musi zostac dokladnie tyle ile kosztuje nas przejscie
                    w = min(10, C[i][0] - C[i][j][0])
                    if f[i] + w >= 0:
                        f[C[i][j][1]] = max(f[C[i][j][1]], f[i] + w)
        
    return f[n-1]
    
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
C = [[2,    [5, 1],     [1, 6],     [1, 8]],        #0
     [2,    [7, 2],     [1, 4],     [1, 2]],        #1
     [89,   [91, 3],    [75, 8],    [84, 6]],       #2
     [8,    [6, 4],     [10, 6],    [7, 5]],        #3
     [4,    [5, 5],     [1, 7],     [3, 5]],        #4
     [10,   [11, 6],    [0, 6],     [4, 6]],        #5
     [1,    [0, 7],     [0, 7],     [6, 7]],        #6
     [57,   [51, 8],    [45, 8],    [50, 8]],       #7
     [2,    [6, 9],     [7, 9],     [0, 9]],        #8
     [6,    [3, -1],    [8, -1],    [1, -1]]]       #9
#print(magic(C))