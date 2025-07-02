from egz3btesty import runtests

def uncool(P):
    n = len(P)
    res = []

    for i in range(n):
        for j in range(i + 1, n):
            a1, a2 = P[i]
            b1, b2 = P[j]
            if a1 < b2 and b1 < a2:
                if not (a1 <= b1 and a2 >= b2) and not (b1 <= a1 and b2 >= a2):
                    return i, j
    
    return res

# Uruchomienie testów
runtests(uncool, all_tests=True)
