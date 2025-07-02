""""Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
będącą liczbą pierwszą?"""


def IsPrime(n):
    if n < 2: return False

    if n == 2: return True

    if n%2 == 0: return False

    i = 3
    while i*i <= n:
        if n%i == 0: return False

    return True

def czy_zawiera_pier(n):

    while n != 0:
        if IsPrime(n%10):
            return True
        n //= 10

    return False

def czy_wiersz(T):
    size = len(T)

    for i in range(size):
        if not czy_zawiera_pier(T[i]): return False

    return True

def main_func(T):
    size = len(T)

    for i in range(size):
        if czy_wiersz(T[i]): return True


    return False


T = [[6, 8, 6], [6, 8, 15], [24, 42, 42]]

print(main_func(T))