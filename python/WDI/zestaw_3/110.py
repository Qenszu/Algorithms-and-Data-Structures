""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
szachowego"""

def main_func(T, q):
    size = len(T)
    cnt = 0

    for i in range(size):
        for j in range(size):
            
            if i-2 >= 0:
                if j-1 >= 0:
                    if T[i][j]*T[i-2][j-1] == q:
                        cnt += 1
                if j+1 < size:
                    if T[i][j]*T[i-2][j+1] == q:
                        cnt += 1
            #end if

            if i-1 >= 0:
                if j+2 < size:
                    if T[i][j]*T[i-1][j+2] == q:
                        cnt += 1
                if j-2 >= 0:
                    if T[i][j]*T[i-1][j-2] == q:
                        cnt += 1
            #end if

            if i+1 < size:
                if j+2 < size:
                    if T[i][j]*T[i+1][j+2] == q:
                        cnt += 1
                if j-2 >= 0:
                    if T[i][j]*T[i+1][j-2] == q:
                        cnt += 1
            #end if

            if i+2 < size:
                if j+1 < size:
                    if T[i][j]*T[i+2][j+1] == q:
                        cnt += 1
                if j-1 >= 0:
                    if T[i][j]*T[i+2][j-1] == q:
                        cnt += 1
            #end if
        #end for
    #end for

    return cnt//2

T = [
    [1, 2, 3, 0],
    [2, 1, 4, 0],
    [1, 2, 1, 0],
    [0, 0, 0, 0]
]

print(main_func(T, 2))






