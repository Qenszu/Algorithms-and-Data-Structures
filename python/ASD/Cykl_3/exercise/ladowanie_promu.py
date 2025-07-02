def ladowanie_promu(T, D):
    n = len(T)
    tab = [[[0 for i in range(D+1)] for j in range(D+1)] for k in range(D+1)]

    def rek(tab, i, j, k):
        if i == 0:
            return True
        
        if j < T[i] and k < T[i]:
            return False
        
        if tab[i][j][k] == 0:
            tab[i][j][k] =  rek(tab, i-1, j-T[i-1], k) or rek(tab, i-1, j, k-T[i-1])

        return tab[i][j][k]

    i = 0
    while i < n and rek(tab, i, D+1, D+1):
        i += 1
    
    return i