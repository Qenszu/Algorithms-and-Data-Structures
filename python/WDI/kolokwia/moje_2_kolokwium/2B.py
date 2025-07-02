def A(n):
    wynik = 0
    while n != 0:
        wynik *= 10
        wynik += n%10
        n //= 10
    return wynik + 1

def is_prime(n):
    if n == 2 or n == 3 or n == 5:
        return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return False
    if n < 2:
        return False
    
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

def B(n):
    while True:
        if is_prime(n+1):
            return n+1
        n += 1

def C(n):
    liczba = float(1/n)
    while liczba < 1:                       #liczba < 0 !!!!!!
        liczba *= 10

    if n == 1:
        return 100
    return int(liczba*100)


def min_len(s1, s2):
    size1 = len(s1)
    size2 = len(s2)

    if size1 < size2:
        return s1
    return s2

def cykl(x):
    tmp = x
    def rek(x, s = "", c = 0):
        nonlocal tmp
        if x == tmp and c != 0 and c < 10:
            return s
        if c == 10:
            return "1234567891011"
        
        return min_len(rek(A(x), s + "A", c + 1), min_len(rek(B(x), s + "B", c + 1), rek(C(x), s + "C", c + 1)))
    return rek(x)

print(cykl(51))