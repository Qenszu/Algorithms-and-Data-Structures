""""Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą 
oraz liczba kawałków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. 
Na przykład: divide(2347)=True, podział na 23 i 47, natomiast divide(2255)=False"""

def prime(n):
    if n == 2:
        return True
    if n < 2 or n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def divide(n, l = 0, p = 0):

    x = False
    result = False
    if n == 0:
        if l != 0:
            if prime(l) and prime(p+1):
                return True
        elif prime(p):
            return True
        else:
            return False
        
    tmp = n
    m = 10

    while tmp != 0:
        if prime(n%m):
            result = divide(n//m, 0, p+1)
            if result:
                x = True
                break
        tmp //= 10
        m *= 10 

    return x

      

print(divide(2255))

    