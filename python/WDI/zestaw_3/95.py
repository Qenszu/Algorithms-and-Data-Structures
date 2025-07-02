""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
element do sumy elementów wiersza w którym leży element jest największa."""


def suma_wiersza(T):
    size = len(T)
    suma = 0

    for i in range(size):   
        suma += T[i]

    return suma

def main_func(T):
    size = len(T)
    max_wiersz = None
    max_kolumna = None
    maxi = 0

    for i in range(size):
        suma_wiersz = suma_wiersza(T[i])

        for j in range(size):
            suma_kolumny = 0

            for a in range(size):
                suma_kolumny += T[a][j]
            #end for a

            if suma_wiersz * suma_kolumny > maxi:
                maxi = suma_wiersz * suma_kolumny
                max_wiersz = i
                max_kolumna = j
        #end for j
    # end for i 

    print(maxi, max_wiersz + 1, max_kolumna + 1)


T = [
[1, 0, 1, 0, 1, 1, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
[1, 1, 0, 0, 0, 1, 1, 1, 0, 1], #max
[0, 1, 0, 0, 1, 1, 0, 1, 1, 0], #1
[1, 0, 1, 1, 0, 1, 1, 0, 1, 0], #2
[1, 1, 1, 1, 1, -7, 1, 1, 1, 1], #3
[1, 0, 0, 1, 1, 1, 0, 0, 1, 1], #4
[0, 1, 1, 0, 0, 1, 1, 1, 0, 0], #5
[1, 1, 0, 1, 0, 1, 1, 0, 1, 1], #6
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1] #min
]

main_func(T)
        








T = [
[1, 0, 1, 0, 1, 1, 0, 0, 1, 0],
[0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
[1, 1, 1, 0, 1, 0, 1, 1, 0, 1], #max
[0, 1, 0, 0, 1, 1, 0, 1, 1, 0], #1
[1, 0, 1, 1, 0, 0, 1, 0, 1, 0], #2
[0, 1, 1, 1, 0, 0, 1, 0, 0, 1], #3
[1, 0, 0, 1, 1, 1, 0, 0, 1, 1], #4
[0, 1, 1, 0, 0, 1, 1, 1, 0, 0], #5
[1, 1, 0, 1, 0, 0, 1, 0, 1, 1], #6
[0, 0, 1, 0, 1, 1, 0, 1, 0, 1] #min
]