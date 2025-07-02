""""Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
przyjaciółkami"""

def are_friends(a, b):
    Ta = [0 for _ in range(10)]
    Tb = [0 for x in range(10)]

    while a != 0:
        Ta[a%10] = 1
        a //= 10

    while b != 0:
        Tb[b%10] = 1
        b //= 10

    if Ta == Tb: return True

    return False

def main_func(T):
    size = len(T)
    cnt = 0

    for i in range(size-1):
        if are_friends(T[size-1][i], T[size-1][i+1]): cnt += 1
        if are_friends(T[size-1][i], T[size-2][i+1]): cnt += 1
        if are_friends(T[i][size-1], T[i+1][size-1]): cnt += 1
        if are_friends(T[size-1][i], T[size-1][i+1]): cnt += 1
        
        for j in range(size-1):
            if are_friends(T[i][j],T[i+1][j+1]): cnt += 1
            if are_friends(T[i][j],T[i+1][j]): cnt += 1
            if are_friends(T[i][j],T[i][j+1]): cnt += 1

            

        

    return cnt


T = [[3, 3, 5],
     [3, 3, 5],
     [3, 3, 5]]

print(main_func(T))
            

    