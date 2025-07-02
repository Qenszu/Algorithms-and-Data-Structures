""""Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporządkowane niemalejąco"""


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

    while index != size*size:
        
        for j in range(size):
            if mini > T1[j][0] and T1[j][0] != -1:
                mini = T1[j][0]
                min_ind = j
        #end for

        T2[index] = mini
        index += 1
        del_elem(T1[min_ind])
        
        mini = max_ele       
    #end for 

    return T2


T1 = [[  1,   3,   9,  12,  24,  33,  34,  38,  46,  88],
 [ 24,  27,  37,  46,  61,  70,  72,  73,  80,  81],
 [  3,  11,  66,  70,  78,  88,  92,  93,  94,  97],
 [  2,  27,  29,  39,  47,  52,  58,  76,  83,  97],
 [ 17,  33,  40,  52,  60,  66,  72,  73,  79,  89],
 [ 14,  26,  36,  53,  59,  72,  74,  77,  88, 100],
 [  8,   9,  13,  28,  38,  44,  60,  65,  97,  98],
 [  1,   2,   5,  15,  25,  43,  46,  47,  64,  69],
 [  6,  39,  43,  46,  54,  59,  73,  74,  75,  95],
 [  7,  11,  18,  28,  29,  38,  49,  83,  95, 100]]

"""T1 = [
    [1, 3, 4, 7],
    [2, 3, 5, 6],
    [6, 9, 11, 13],
    [3, 6, 8, 15]
]"""


print(main_func(T1))


            



        
            
