"""Problem 8 Hetmanów"""

def zakres(T, i, j, a):

    for k in range(8):
        T[k][j] += a
    
    k = 1
    while i+k < 8 and j+k < 8:
        T[i+k][j+k] += a
        k += 1
    k = 1
    while i+k < 8 and j-k > -1:
        T[i+k][j-k] += a
        k += 1

    T[i][j] += 9*a


def rek(T, i = 0):
    if i == 8:
        for x in range(8):
            print(T[x])
        return True
    

    for j in range(8):
        if T[i][j] == 0:
            zakres(T, i, j, 1)
            if rek(T, i + 1):
                return True
            zakres(T, i, j, -1)

    return False
T = [[0 for h in range(8)]for b in range(8)]
print(rek(T))


