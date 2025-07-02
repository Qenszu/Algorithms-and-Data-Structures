""""Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
powinny zawierać zera."""

def del_elem(T):
    size = len(T)

    for i in range(size - 1):
        T[i] = T [i + 1]

    T[size-1] = -1

    return T

def znajdz_max(T):
    size = len(T)
    maxi = 0

    for i in range(size):
        maxi = max(T[i][size-1], maxi)

    return maxi


def main_func(T1):
    size = len(T1)
    T2 = [0 for _ in range(size*size)]
    max_ele = znajdz_max(T1)
    minimum = None
    min_ind = 0
    mini = T1[0][0]
    licz = 0
    index = 0

    while licz != size:
        licz = 0
        czy_pominac = False
        
        for j in range(size):
            if T1[j][0] == -1:
                licz += 1

            elif mini > T1[j][0] and T1[j][0] != -1:
                mini = T1[j][0]
                min_ind = j

            elif mini == T1[j][0] and min_ind != j:

                czy_pominac = True
                del_elem(T1[j])
                if T1[min_ind][0] == mini:
                    del_elem(T1[min_ind])
        #end for

        if not czy_pominac:
            T2[index] = mini
            index += 1
            del_elem(T1[min_ind])
        
        mini = max_ele       
    #end for 

    return T2


T1 = [
    [1, 3, 4, 7],
    [2, 3, 5, 6],
    [6, 9, 11, 13],
    [3, 6, 8, 15]
]

print(main_func(T1))


            



        
            
