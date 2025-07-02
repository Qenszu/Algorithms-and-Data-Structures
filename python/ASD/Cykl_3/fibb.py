def fibb(n):
    F = [1 for _ in range(n+1)]
    F[0] = 0
    F[1] = 1

    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    
    print(F)
    return F[n]

print(fibb(10))