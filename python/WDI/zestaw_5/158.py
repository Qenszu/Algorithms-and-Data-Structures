""""Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać
na pola o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz
funkcję, która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie
da, zwraca -1."""
from math import sqrt

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i < sqrt(n+1) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


def func(T):
    result = -1
    mini = float("inf")
    def rek(T, i = 0, jumps = 0):
        nonlocal result, mini
        size = len(T)

        if i == size - 1:
         if jumps < mini:
            result = jumps
            mini = jumps
        if i >= size:
            return

        for k in range(int(sqrt(T[i])) + 2, 1, -1):
            if is_prime(k) and i + k < size:
                rek(T, i + k, jumps + 1)
    rek(T)
    print(result)

T = [4, 2, 10, 2, 1, 4, 1, 1]
func(T)


