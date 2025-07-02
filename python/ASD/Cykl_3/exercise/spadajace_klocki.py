def fall(a, b, c, d):
    return a >= c and b <= d

def bricks(T):
    n = len(T)
    F = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if fall(T[i][0], T[i][1], T[j][0], T[j][1]):
                F[i] = max(F[i], F[i] + 1)

    return max(F)
    