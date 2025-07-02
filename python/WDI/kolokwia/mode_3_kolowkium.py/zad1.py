def bridge(T):
    min_koszt = float("-inf")
    size = len(T)
    min_wyspy = (0,0)
    for i in range(size):
        for j in range(size):
            if T[i][j] > 0:
                wyspa = T[i][j]
                koszt = 0
                if i + 1 != size:
                    w = i + 1
                    while T[w][j] == T[i][j]:
                        w += 1
                    while w + 1 != size and T[w+1][j] < 0:
                        koszt += T[w][j] #!!!!!! w + 1
                        if w + 2 == size:
                            break
                        w += 1
                    koszt += T[w][j] #!!!!!! brak
                    if T[w+1][j] > 0:
                        if min_koszt < koszt:
                            min_koszt = koszt
                            min_wyspy = (wyspa, T[w+1][j])
                koszt = 0
                if j+1 != size:
                    k = j + 1
                    while T[i][k] == T[i][j]:
                        k += 1
                    while k + 1 != size and T[i][k+1] < 0:
                        koszt += T[i][k] #!!!!!! k + 1
                        if k+2 == size:
                            break
                        k += 1
                    koszt += T[i][k] #!!!!!! brak
                    if k + 1 == size:    #TUUU
                        k -= 1   
                    #print(koszt, wyspa, T[i][k+1])        #TUUUU
                    if T[i][k+1] > 0:
                        if min_koszt < koszt:
                            min_koszt = koszt
                            min_wyspy = (wyspa, T[i][k+1])
    return min_wyspy

T = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
     [-1, 1, 1,-1,-5,-5, 4, 4, 4,-1,-1,-1],
     [-1, 1, 1, 1,-5,-5, 4, 4, 4,-1,-1,-1],
     [-1, 1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
     [-1,-1,-7,-8, 3, 3,-1,-1,-7,-1,-1,-1],
     [-1,-1,-1, 3, 3, 3,-1,-1,-1,-1,-1,-1],
     [-1,-1,-6,-6,-1,-1,-1,-1, 5, 5, 5,-1],
     [-1,-1, 2, 2,-1,-2,-1,-10, 5, 5, 5,-1],
     [-1,-1, 2, 2,-1,-1,-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
]

print(bridge(T))