def frog(A):
    n = len(A)
    F = [0 for _ in range(n)]
    R = [0 for _ in range(n)]
    F[0] = 0

    for i in range(1, A[0]+1):
        F[i] = 1
        R[i] = A[0] - i

    b = 1
    for i in range(A[0]+1, n):
        if R[i-1] != 0:
            F[i] = F[i-1]
            R[i] = R[i-1] - 1
        else:
            F[i] = F[i-1] + 1
            for j in range(b, i):
                R[i] = max(R[i], R[j] + A[j] - (i-j))
            b = i
    
    return F[n-1]