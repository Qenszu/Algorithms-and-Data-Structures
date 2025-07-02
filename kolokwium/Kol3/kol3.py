"""
Patryk Opala
Program sprawdza obciecie blatu z gory i z dolu i decyduje sie na obciecie blatu 
tam gdzie suma seków jest nie wieksza od s oraz tam gdzie ta suma jest najblizsza wartosci s
czyli w danym cieciu eliminuje maksymalną ilość sęków
zlozonosc czasowa: O(n + m)
"""

from kol3testy import runtests

def parkiet(B, C, s):
    n = len(C)
    m = len(C[0])
    a = 0
    b = 0
    cnt = 0
    

    for i in range(n + m):
        if C[a][b] <= s:
            if a == n-1 or b == n-1:
                break
        x = float("inf")
        y = float("inf")
        if a + 1 < n:
            x = C[a][b] - C[a+1][b]
        if b + 1 < n:
            y = C[a][b] - C[a][b+1]
        if x > s and y > s:
           return -1
        else:
            if y >= x:
                cnt += 1
                a += 1
            else:
                cnt += 1
                b += 1
        
    return cnt

#POPRAWNE

"""
def parkiet(B, C, s):
    n = len(C)
    m = len(C[0])

    f = [[float("inf") for _ in range(m)] for h in range(n)]
    f[0][0] = 0
    result = float("inf")

    for i in range(n):
        for j in range(m):
            if C[i][j] <= s and f[i][j] != float("inf"):
                return f[i][j]
            if f[i][j] != float("inf"):
                if j + 1 < m and C[i][j] - C[i][j+1] <= s:
                    f[i][j+1] = min(f[i][j]+1, f[i][j+1])
                if i + 1 < n and C[i][j] - C[i+1][j] <= s:
                    f[i+1][j] = min(f[i][j]+1, f[i+1][j])


    if f[n-1][m-1] == float("inf"):
        return -1
    
    return f[n-1][m-1]
B = [[2, 1, 4], 
     [1, 3, 1], 
     [2, 3, 3]]                   
C = [[20, 15, 8], 
     [13, 10, 4], 
     [8, 6, 3]]
s = 5
"""

#print(parkiet(B, C, s))

runtests(parkiet, all_tests = True)
