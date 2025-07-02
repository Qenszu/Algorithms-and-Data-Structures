""""Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi,
    zwraca wartość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje 
    co najmniej jedno 0 oraz wartość False w przeciwnym przypadku."""

def czy_0_wierszu(T):
    size = len(T)

    for i in range(size):
        if T[i] == 0: return True

    return False


def main_func(T):
    size = len(T)

    for a in range(size):
        if not czy_0_wierszu(T[a]): return False

    for i in range(size):
        czy_0 = False
        
        for j in range(size):
            if T[j][i] == 0: czy_0 = True
        #end for

        if not czy_0: return False
    #end for

    return True

T = [[0, 1, 0],
     [1, 1, 1],
     [1, 0, 1]]

print(main_func(T))
        

