def sprawdz(T):
    size = len(T)

    for i in range(size):
        cnt = 0
        for a in range(1, 10):
            for j in range(size):
                if T[i][j] == a:
                    cnt += 1
                    break
        if cnt != 9:
            return False
    
    for l in range(size):
        cnt = 0
        for k in range(1, 10):
            for b in range(size):
                if T[b][l] == k:
                    cnt += 1
                    break
        if cnt != 9:
            return False

    return True

def sudoku(N, cube1, cube2):
    T = N
    for i in range(3):
        for j in range(3):
            T[((cube1-1)//3)*3+i][(cube1%3)*3+j], T[((cube2-1)//3)*3+i][(cube2%3)*3+j] = T[((cube2-1)//3)*3+i][(cube2%3)*3+j], T[((cube1-1)//3)*3+i][(cube1%3)*3+j]

    return T

N=[
    [8,1,2,7,5,3,6,4,9],
    [9,4,3,6,8,2,1,7,5],
    [6,7,5,4,9,1,2,8,3],
    [1,5,4,3,6,8,8,9,6],
    [3,6,9,9,1,7,7,2,1],
    [2,8,7,4,5,2,5,3,4],
    [5,2,1,9,7,4,2,3,7],
    [4,3,8,5,2,6,8,4,5],
    [7,9,6,3,1,8,1,6,9]]


for i in range(1, 10):
    for j in range(i+1, 10):
        if sprawdz(sudoku(N, i-1, j-1)):
            print(i, j)
        else:
            N = sudoku(N, i - 1, j - 1)




         

