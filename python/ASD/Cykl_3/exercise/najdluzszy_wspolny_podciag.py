def fun(A, B):
    F = []
    
    for n in range(len(A)+1):
        F.append([])
        for k in range(len(B)+1):
            F[n].append([])
        
    def _F_(n,k):
        if A[n] == B[k]:
            return _F_(n-1, k-1) + 1
        else:
            return 
        

#5 1 1 1 1 1 4 4 4