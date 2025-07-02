#Longest increasing subsequence

def lis(A):
    n = len(A)
    F = [1 for _ in range(n)]
    maxi = 0
    P = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[j] + 1 > F[i]:
                F[i] = F[j] + 1
                P[i] = j
        
        if F[i] > F[maxi]:
            maxi = i
    
    return maxi, F, P

#A = [7, 3, 4, 2, 6, 9, 5, 9, 1]
A = [1, 2, 3, 4]
print(lis(A))