""""Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
maksymalnego podciągu"""

def sum_poem(T):
    size = len(T)
    maxi = 0

    for i in range(size-1):
        sume = 0
        for j in range(10):
            if i+j == size:
                break

            sume += T[i+j]
        #end for
        maxi = max(sume, maxi)
    #end for

    return maxi

def sum_column(T, c):
    size = len(T)
    maxi = 0

    for i in range(size):
        sume = 0
        for j in range(10):
            if i+j == size:
                break 
            
            sume += T[i+j][c]
        #end for
        maxi = max(maxi, sume)
    #end for

    return maxi

def main_func(T):
    size = len(T)
    maxi = 0

    for i in range(size):
        maxi = max(sum_poem(T[i]), maxi)
        for j in range(size):
            maxi = max(sum_column(T, j), maxi)

    return maxi

T = [[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 16, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 5, 5, 7, 0],
     [0, 0, 0, 12, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]]
            
print(main_func(T))




            