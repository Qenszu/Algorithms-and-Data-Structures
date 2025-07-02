def SubSum(A, T):
    n = len(A)
    dp = [[False for _ in range(T+1)] for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, T+1):
            if dp[i-1][j]:
                dp[i][j] = True
            if j - A[i-1] >= 0 and dp[i-1][j - A[i-1]]:
                dp[i][j] = True
    
    return dp[n][T]

A = [1, 2, 3, 4]
T = 20
print(SubSum(A, T))




