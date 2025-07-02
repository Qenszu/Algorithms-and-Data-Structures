
end = None
def IsPrime(n):
    i = 3
    if n%2 == 0 and n != 2:
        return False
    while i**i <=n:
        if n%i == 0:
            return False
        i += 1
        
    return True

def func(tab):
    size = len(tab)
    i = 0
    j = 1
    pom = False

    for a in range(size):
        if a == i and IsPrime(tab[i]):
            return False
        elif IsPrime(tab[a]):
            pom = True
        i, j = j, i + j
        
    if pom:
        return True
    else:
        return False
    
tab = [6, 6, 4, 8, 8, 6, 8]
print(func(tab))
    
