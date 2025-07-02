"""Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
[5, 7, 15] → f alse, podział nie istnieje."""

def sum_of_one(n):
    sum = 0

    while n != 0:
        sum += n%2
        n //= 2

    return sum

def rek(T, i = 0, a = 0, b = 0, c = 0):
    size = len(T)
    if i == size:
        return a == b == c
    
    sum = sum_of_one(T[i])

    return rek(T, i + 1, a + sum, b, c) or rek(T, i + 1, a, b + sum, c) or rek(T, i + 1, a, b, c + sum)
    
    
T = [5, 7, 15]

print(rek(T))
    

