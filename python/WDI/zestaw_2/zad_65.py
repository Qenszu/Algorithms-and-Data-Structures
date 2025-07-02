end = None
def czy_nie_posiada_niep(x):
    while x != 0:
        if (x%10)%2 != 0:
            return False
        x //= 10
    end

    return True

def func(n):
    tab = [i for i in range(1, n + 1)]

    pom = True
    for j in range(n):
       if czy_nie_posiada_niep(tab[j]):
           print("Nie wszystkie zawieraja cyfre nieparzysta")
           pom = False
           break
    end

    if pom: 
        print("Wszystkie maja cyfre nieparzysta")

func(50) 