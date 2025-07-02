""""Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
będących liczbami pierwszymi?"""

def IsPrime(n):
    if n < 2: return False

    if n == 2: return True

    if n%2 == 0: return False

    i = 3
    while i*i <= n:
        if n%i == 0: return False

    return True

def czy_cala_pier(n):

    while n != 0:
        if not IsPrime(n%10):
            return False
        n //= 10

    return True

def czy_wiersz(T):
    size = len(T)

    for i in range(size):
        if czy_cala_pier(T[i]): return True

    return False

def main_func(T):
    size = len(T)

    for i in range(size):
        if not czy_wiersz(T[i]): return False


    return True


T = [[2, 8, 6], [6, 2, 15], [2, 42, 42]]

print(main_func(T))