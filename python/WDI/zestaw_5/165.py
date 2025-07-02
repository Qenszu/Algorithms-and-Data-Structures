""""Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, 
    która odpowiada na pytanie, czy spośród (niekoniecznie wszystkich) elementów 
    tablicy można utworzyć dwa podzbiory o jednakowej sumie elementów, tak aby suma 
    mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać wyłącznie tablicę T oraz 
    liczbę naturalną k, funkcja powinna zwrócić wartość typu bool."""

def rek(T, k, s1 = 0, s2 = 0, i = 0, m = 0):
    if i > len(T):
        return False
    if k == m:
        return s1 == s2
    
    else:
        return rek(T, k, s1 + T[i], s2, i + 1, m + 1) or rek(T, k, s1, s2 + T[i], i + 1, m + 1) or rek(T, k, s1, s2, i+1, m) 
    
T = [2, 2, 3]
k = 2
print(rek(T, k))
