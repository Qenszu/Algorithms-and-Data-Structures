from zad8testy import runtests

"""
Algorytm wykorzystuje mechaniz sortowania oparty na countsort
Nastepnie zlicza odpowiednio najwieksze wartosci dopoki sie one "nie roztopia"
"""

def ice_cream(T):
    MAX_L = max(T) if T else 0
    count = [0] * (MAX_L + 1)

    for val in T:
        count[val] += 1

    result = 0
    minute = 0


    for val in range(MAX_L, -1, -1):
        while count[val] > 0:
            eaten = max(0, val - minute)
            result += eaten
            minute += 1
            count[val] -= 1

    return result



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
