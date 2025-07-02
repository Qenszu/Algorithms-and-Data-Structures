def pokrewne5(n1, n2):
    T1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    T2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while n1 != 0:
        T1[n1%5] = 1
        n1 //= 5

    while n2 != 0:
        T2[n2%5] = 1
        n2 //= 5

    return T1 == T2

def czy_szczesliwe(T, w, k, N):
    cnt = 0
    if w-2 > -1 and k-2 > -1:
        ind_w = w-2
        ind_k = k-2
    elif w - 1 > -1 and k - 2 > -1:
        ind_w = w - 1
        ind_k = k - 2
    elif w - 2 > -1 and k - 1 > -1:
        ind_w = w - 2
        ind_k = k - 1
    if w + 2 < N and  k + 2 < N:
        x = w + 2
        y = k + 2
    elif w + 1 < N and  k + 2 < N:
        x = w + 1
        y = k + 2
    elif w + 2 < N and k + 1 < N:
        x = w + 2
        y = k + 1
    print(ind_w, ind_k, x, y)
    h = 1
    for i in range(ind_w, x):
        for j in range(ind_k, y):
            print(h, i , j)
            h += 1
            if pokrewne5(T[w][k], T[i][j]):
                cnt += 1

    
    return cnt == 18

def luck17(T):
    size = len(T)

    for i in range(1, size-1):
        cnt1 = 0
        cnt2 = 0
        for j in range(1, size-1):
            if i == 1 and j == 1:
                continue
            if i == 1 and j == size - 2:
                continue
            if i == size - 2 and j == 1:
                continue
            if i == size - 2 and j == size - 2:
                continue
            print(i, j)
            if czy_szczesliwe(T, i, j, size):
                print("Jest")
                cnt1 += 1
            if czy_szczesliwe(T, j, i, size):
                cnt2 += 1
                print("Jest")

        if cnt1 > 1 or cnt2 > 1:
            return True
    
    return False

T = [
    [6, 6, 6, 6, 6],
    [5, 5, 5, 5, 6],
    [5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5],
    [6, 5, 5, 5, 5]
]

print(czy_szczesliwe(T, 3, 2, 5))

#print(luck17(T))