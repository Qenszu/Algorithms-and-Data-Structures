def func(T):
    min_res = float("inf")
    def rek(T, el_sum = 0, ind_sum = 0, ind = 0):
        nonlocal min_res
        if el_sum == ind_sum and el_sum != 0:
            if min_res > el_sum:
                min_res = el_sum
        if ind == len(T):
            return 
        if T[0] == 0:
            return 0
    
        rek(T, el_sum, ind_sum, ind + 1)
        rek(T, el_sum + T[ind], ind_sum + ind, ind + 1)

    rek(T)
    return min_res

T = [1, 7, 3, 5, 11, 2]

print(func(T))


    
