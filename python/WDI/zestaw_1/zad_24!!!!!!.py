from math import sqrt
end = None

def IsPrime(x):
    if x == 2:
        return True
    if x%2 == 0:
        return False
    
    for i in range(3, int(sqrt(x) + 1)):
        if x%i == 0:
            return False
    end

    return True

def extended(x, n, index, mnoznik):
    if index == 9:
        return None
    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    zapas = x
    mnoznik *= 100
    zapas *= 10
    zapas += tab[index]*mnoznik + tab[index]
    print(zapas)
    

    if IsPrime(zapas) and zapas < n:
        print(zapas)
        extended(zapas, n, ++index, mnoznik)
    if zapas > n and index != 9:
        extended(x, n, ++index, mnoznik)
    else:
        return None
    

    while False:
        pom = zapas
        zapas *= 10
        zapas += tab[index]*mnoznik + tab[index]
        print(zapas)
        if zapas > n:
            extended(pom, n, ++index)
        if IsPrime(zapas):
            print(zapas)
            extended(zapas, n)
        mnoznik *= 100
        pom = zapas
    end
    
def func(n):
    tab = [2, 3, 5, 7]
    i = 0

    while i < 4:
        print("tu", tab[i])
        extended(tab[i], n, 0, 1)
        i += 1
    
        


func(1000)