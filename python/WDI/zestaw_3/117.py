def func(T):
    size = len(T)
    cnt = 2
    result = 0

    for i in range(size):
        for j in range(size - 2):
            tmp_j = j
            if T[i][j] + T[i][j+1] == T[i][j+2] and T[i][j+1] != 0:
                cnt = 2
                while tmp_j+2 < size:
                    if T[i][tmp_j] + T[i][tmp_j+1] == T[i][tmp_j+2]:
                        cnt += 1
                        tmp_j += 1
                        result = max(result, cnt)
                    else:
                        break
            tmp_j = j
            if T[i][j+2] + T[i][j+1] == T[i][j] and T[i][j+1] != 0:
                cnt = 2
                while tmp_j + 2 < size:
                    if T[i][tmp_j+2] + T[i][tmp_j+1] == T[i][tmp_j]:
                        cnt += 1
                        tmp_j += 1
                        result = max(result, cnt)
                    else:
                        break
    return result

T = [[0, 2, 3, 5], [0, 0, 0, 0], [5, 3, 2, 1], [0, 0, 0, 0]]
print(func(T))
                        


