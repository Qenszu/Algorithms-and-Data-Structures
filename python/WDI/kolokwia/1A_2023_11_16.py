from math import sqrt

def czy_pierwsza(n):
    if n == 2:
        return True
    elif n%2 == 0:
        return False 
    for i in range(3, int(sqrt(n))+1, 2):
        if n%i == 0:
            return False
    return True

def zgodne(T):
    dlugosc = len(T)
    pom_tab = T                             #jest to pomocnicza tabela rowna tabeli poczatkowej
    for i in range(2,dlugosc - 1):
        for j in range(-2, 3):
            if j == 0:
                continue
            else:
                x = 1

