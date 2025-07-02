"""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
parzystą"""

def if_have_even(n):

    while n != 0:
        if (n%10) % 2 == 0:
            return 1
        n //= 10

    return 0

def number_of_even(T):
    size = len(T)
    cnt = 0

    for i in range(size):
        cnt += if_have_even(T[i])

    if cnt != 0:
        return True
    
    return False

def main_func(T):
    size = len(T)

    for i in range(size):
        if not number_of_even(T[i]):
            return False
    
    return True
        
T = [[1, 1, 3], [2, 4, 5], [1, 1, 1]]

print(main_func(T))

