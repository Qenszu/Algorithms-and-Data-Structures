from math import sqrt

def sito(n):
    tablica = [0 for i in range(n+1)]
    j = 2

    while j <= sqrt(n):
        i = j
        mnoznik = 2
        while i*mnoznik <= n:
            tablica[i*mnoznik] = 1
            mnoznik += 1
        j += 1

    for a in range(2, n+1):
        if tablica[a] == 0:
            print(a)


sito(16)