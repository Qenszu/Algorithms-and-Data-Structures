from egz1atesty import runtests

def snow(S):
    S.sort(reverse=True)  
    total = 0
    day = 0

    for snow in S:
        remaining = snow - day
        if remaining <= 0:
            break
        total += remaining
        day += 1

    return total



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
