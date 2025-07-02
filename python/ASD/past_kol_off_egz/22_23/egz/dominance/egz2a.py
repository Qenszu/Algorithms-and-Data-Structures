from egz2atesty import runtests

def dominance(P):
    n = len(P) 
    Y = [0 for _ in range(n + 1)]
    X = [0 for _ in range(n + 1)]

    for x, y in P:
        Y[y] += 1
        X[x] += 1

    for i in range(n, 0, -1):
        Y[i-1] += Y[i]
        X[i-1] += X[i]

    min_dom = float("inf")


    for x, y in P:
        dom = X[x] + Y[y]
        min_dom = min(min_dom, dom) 

    return n - min_dom + 1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

