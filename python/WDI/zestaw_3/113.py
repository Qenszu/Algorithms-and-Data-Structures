"""""Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy
jako liczbę zapisaną w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000. Proszę zaimplementować funkcję distance(T), która 
dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartychw wierszach liczb jest największa. Do funkcji należy przekazać 
tablicę, funkcja powinna zwrócić odległość pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają
identycznego ciągu cyfr."""

def maxi(T1, T2):
    size = len(T1)

    for i in range(size):
        if T1[i] > T2[i]:
            return T1
        elif T1[i] < T2[i]: 
            return T2
        
def mini(T1, T2):
    size = len(T1)

    for i in range(size):
        if T1[i] < T2[i]:
            return T1
        elif T1[i] > T2[i]:
            return T2       


def distance(T):
    size = len(T)
    maximum = maxi(T[0], T[1])
    max_ind = 0
    minimum = min(T[0], T[1])
    min_ind = 0

    for i in range(2, size):
        if maximum != maxi(maximum, T[i]):
            max_ind = i
            maximum = maxi(maximum, T[i])


        if minimum != mini(minimum, T[i]):
            min_ind = i
            minimum = mini(minimum, T[i])
            

    print(abs(max_ind - min_ind))


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

distance(T)