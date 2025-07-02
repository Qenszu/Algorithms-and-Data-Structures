""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
się znaleźć taki ciąg oraz długość tego ciągu."""


def czy_ciag_geo(a1, a2, a3):
    if a1*a3 == a2*a2 and a1 != 0 and a2 != 0 and a3 != 0: return True

    return False

def main_func(T):
    size = len(T)
    maxi = 2  

    for j in range(size - 2):
        obecny_ciag_1 = 2
        obecny_ciag_2 = 2

        for i in range(size - 2 - j):

            if czy_ciag_geo(T[i][i+j], T[i+1][i+j+1], T[i+2][i+j+2]):
                obecny_ciag_1 += 1
            else:
                obecny_ciag_1 = 2
            maxi = max(maxi, obecny_ciag_1)
        #end for

        for a in range(size - 2 - j):

            if czy_ciag_geo(T[a+j][a], T[a+j+1][a+1], T[a+j+2][a+2]):
                obecny_ciag_2 += 1
            else:
                obecny_ciag_2 = 2
            maxi = max(maxi, obecny_ciag_2)
        #end for
    #end for 

    if maxi == 2: return False
    
    return maxi

T = [[2, 3, 0, 3, 0, 0], 
     [0, 16, 0, 0, 0, 0], 
     [0, 0, 8, 7, 0, 12],
     [2, 0, 0, 4, 0, 0], 
     [0, 0, 0, 0, 2, 0], 
     [0, 0, 8, 0, 0, 0]]

print(main_func(T))

        