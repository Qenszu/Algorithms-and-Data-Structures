""""Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi"""

def sum_poem(T):
    size = len(T)
    maxi = 0

    for i in range(size-1):
        sume = 0
        for j in range(10):
            if i+j == size:
                break

            sume += T[i+j]
        #end for
        maxi = max(sume, maxi)
    #end for

    return maxi

def sum_column(T, c):
    size = len(T)
    maxi = 0

    for i in range(size):
        sume = 0
        for j in range(10):
            if i+j == size:
                break 
            
            sume += T[i+j][c]
        #end for
        maxi = max(maxi, sume)
    #end for

    return maxi

def main_func(T):
    size = len(T)
    maxi = [0, 0]
    p1 = None
    p2 = None
    c1 = None
    c2 = None

    for i in range(size):
        sume = 0

        if maxi[1] > maxi[0]:
            maxi[1], maxi[0] = maxi[0], maxi[1]
            p1, p2 = p2, p1
            c1, c2 = c2, c1
        #end if

        for j in range(size):
            sume = (sum_poem(T[i]) - T[i][j]) + (sum_column(T, j) - T[i][j])
            if sume > maxi[1]:
                maxi[1] = sume
                p2 = i
                c2 = j
            #end if
        #end for
    #end for

    print(maxi[0], p1+1, c1+1)
    print(maxi[1], p2+1, c2+1)

"""T = [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 6],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 2]]"""

T = [[4,0,2],
     [3,0,0],
     [6,5,3]]

main_func(T)