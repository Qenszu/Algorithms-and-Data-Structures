""""Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest
    tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje
    elementy nie posiadające liczby komplementarnej."""

def IsPrime(n):
    if n == 2: return True

    if n%2 == 0: return False

    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    
    return True


def czy_komp(a, b):
    if IsPrime(a+b): return True

    return False

def func(T, i, j):
    size = len(T)

    for a in range(size):
        for b in range(size):
            if i != a or j != b:
                if czy_komp(T[i][j], T[a][b]):
                    return True
    
    
    return False

    

def main_func(T):
    size = len(T)
    T2 = [[0 for _ in range(size)] for x in range(size)]

    for i in range(size):
        for j in range(size):
            if func(T, i, j):
                T2[i][j] = T[i][j]

    print(T2)

T = [[1, 22],
     [2, 13]]

main_func(T)


            
                        