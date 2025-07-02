""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr."""

def if_only_odd(n):
    
    while n != 0:
        if (n % 10) % 2 == 0:
            return False
        n //= 10
    #end while

    return True

def everyone_have_odd(T):
    size = len(T)

    for i in range(size):
        if if_only_odd(T[i]):
            return 1
    #end for

    return 0

def main_func(T):
    size = len(T)
    cnt = 0

    for j in range(size):
        cnt += everyone_have_odd(T[j])

    if cnt == size:
        return True
    
    return False

    

#T = [[j * 10 + _ + 1 for _ in range(10)] for j in range(10)]
T = [[1, 2, 3, 4], [3, 13, 2, 3]]


print(main_func(T))




