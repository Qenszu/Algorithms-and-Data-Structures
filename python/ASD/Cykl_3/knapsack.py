def kanpsack(W, P, B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    T = [0 for i in range(n)] 

    for b in range(W[0], B+1):
        F[0][b] = P[0]

    
    for b in range(B+1):
        for i in range(1, n):
            F[i][b] = F[i-1][b]
            
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i-1][b - W[i]] + P[i])
    ind = B
    for i in range(n - 1, 0, -1):
        if F[i][ind] != F[i-1][ind]:
            T[i] = 1
            ind -= W[i]
    if ind >= W[0] and F[0][ind] == P[0]:  
        T[0] = 1
            
    print(T)
    return F[n-1][B]

W = [4, 2, 3, 1, 3]
P = [5, 3, 4, 2, 2]
B = 7

print(kanpsack(W, P, B))