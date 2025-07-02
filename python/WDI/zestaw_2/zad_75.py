end = None
def func(tab):
    size = len(tab)
    mini_index = 0
    maxi_index = 0

    for i in range(1, size):
        if tab[i] < tab[mini_index]:
            mini_index = i
        elif tab[i] > tab[maxi_index]:
            maxi_index = i
    end

    for j in range(size):
        if j != mini_index:
            if tab[j] == tab[mini_index]:
                return False
        if j != maxi_index:
            if tab[j] == tab[maxi_index]:
                return False
    end

    return True

tab = [1, 2, 3, 4, 1, 5, 7, 8]
print(func(tab))            

