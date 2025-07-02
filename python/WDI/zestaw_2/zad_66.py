end = None
def czy_same_niep(x):
    while x != 0:
        if (x%10)%2 == 0:
            return False
        x //= 10
    end

    return True

def func(n):
    tab = [i for i in range(2, 2*n + 2, 2)]

    for i in range(n):
        if czy_same_niep(tab[i]):
            return True
    end

    return False

if func(40):
    print("Posiada element z samymi nieparzystymi cyframi")
else:
    print("Nie posiada element z samymi nieparzystymi cyframi")