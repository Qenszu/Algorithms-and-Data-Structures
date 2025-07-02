"""Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników. 
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2."""

def rek(n, s = "", ind = 1, loop = 0):

    if n == 0:
        print(s[:-1])

    if n > 0:
        for i in range(ind, n+1):
            if i != n or loop != 0:
                rek(n-i, s + str(i) + "+", i, loop + 1)
    


rek(7)