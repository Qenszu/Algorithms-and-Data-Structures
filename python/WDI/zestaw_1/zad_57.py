from math import log
end = None
def IsPrime(n):
    if n == 2:
        return True
    if n%2 == 0 or n < 2:
        return False
    i = 2
    while i**i < n:
        if n%i == 0:
            return False
        i += 1
    end
    return True


def rotacja(n):
    y = False
    x = False
    if n%10 == 0:
        x = True
    if n < 0:
        y = True 
        n = -n 
    result = n%10
    if y:
        result *= 10
    mnoznik = 10**(int(log(n, 10)))
    result *= mnoznik
    result += n//10

    if x:
        return -result
    return result

def rozklad(n, podst):
    if n < 0:
        n = -n
    iloczyn = 1
    while n != 0:
        iloczyn *= n%podst
        n //= podst
    end

    return iloczyn


def iloczynowo_pierwsza(n):
    size = int(log(n, 10) + 1)
    for i in range(2, 17):
        for j in range(size):
            if IsPrime(rozklad(n, i)):
                return i
            else:
                n = rotacja(n)
        end
    end

    return None


for i in range(4, 20):
   print(f'Dla liczby {i} liczba iloczynowo-pierwsza jest w systemie {iloczynowo_pierwsza(i)}')




