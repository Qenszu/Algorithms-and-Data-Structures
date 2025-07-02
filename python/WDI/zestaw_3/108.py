""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa"""

def main_func(T):
    size = len(T)
    maxi = 0

    for i in range(size):
        for j in range(size):
            suma = 0

            if i+1 < size: 
                suma += T[i+1][j]
                if j+1 < size:
                    suma += T[i+1][j+1]
            #end if

            if j+1 < size:
                suma += T[i][j+1]
                if i != 0:
                    suma += T[i-1][j+1]
            #end if

            if i != 0:
                suma += T[i-1][j]
                if j != 0:
                    suma += T[i-1][j-1]
            #end if

            if j != 0:
                suma += T[i][j-1]
                if i+1 < size:
                    suma += T[i+1][j-1] 
            #end if
            
            maxi = max(maxi, suma)
        #end for
    #end for

    

    return maxi

T = [[1, 1, -1, 1, 1],
     [1, 80, -1, 1, 1],
     [-1, -1, 1, 1, -6],
     [-100, -10, 1, 1, 1],
     [1, 1, -3, 1, 2]]

print(main_func(T))