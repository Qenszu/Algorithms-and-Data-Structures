from egz1Atesty import runtests
from collections import deque

def battle(P, K, R):
    size_P = len(P)
    size_K = len(K)

    n = 0
    n = max(n, max(P))
    n = max(n, max(K))
    n += 1
    
    tab = [0] * n

    q = deque()

    for i in range(size_K):
        tab[K[i]] = R[i]

    for i in range(size_P):
        tab[P[i]] = -1

    cnt = 0
    for i in range(len(tab) - 1, -1, -1):
        if tab[i] == -1:
            q.appendleft(i)
        if tab[i] > 0 and q:
            pro = q.popleft()
            if i + tab[i] >= pro:
                cnt += 1
            else:
                q.appendleft(pro)
        
    return cnt
"""
def battle(P,K,R):
    # tu prosze wpisac wlasna implementacje
    size_P = len(P)
    size_K = len(K)

    for i in range(size_K):
        K[i] = (K[i], R[i])

    for i in range(size_P):
        P[i] = (P[i], True)

    tab = [(0, 0) for _ in range(size_P + size_K)]

    size_tab = size_K + size_P
    for i in range(size_P):
        tab[i] = P[i]
    ind_k = 0
    for i in range(size_P, size_tab):
        tab[i] = K[ind_k]
        ind_k += 1

    tab.sort()
    #print(tab)
    cnt = 0

    for i in range(size_tab - 1, -1, -1):
        if tab[i][1] != False and tab[i][1] != True:
            r = tab[i][1]
            #print("r ", r)
            #print("zasieg", tab[i][0] + tab[i][1])
            ind_p = i + 1
            while ind_p < size_tab and tab[ind_p][0] <= tab[i][0] + r:
                if tab[ind_p][1] == True:
                    tab[ind_p] = (tab[ind_p][0], False)
                    cnt += 1
                    break
                ind_p += 1    
               # print(ind_p)
    #print("lol")
    return cnt

"""
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )

P = [14, 16, 0, 6, 10, 8]
K = [2, 12, 4]
R = [8, 5, 3]
#print(battle(P, K, R))