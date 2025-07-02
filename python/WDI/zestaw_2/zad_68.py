end = None
def najdl_ciag(tab, n):
    max_dl_ciagu = 0
    for i in range(n - 1):
        dl_ciagu = dlugosc_ciagu(tab, i, n)
        if max_dl_ciagu < dl_ciagu:
            max_dl_ciagu = dl_ciagu
    end

    return max_dl_ciagu

def dlugosc_ciagu(tab, index, n):
    dl_ciagu = 1
    while index < n:
        if tab[index + 1] > tab[index]:
            dl_ciagu += 1
            index += 1
        else:
            break
    end
    
    return dl_ciagu

tab = [1, 2, 3, 4, 5, 6, 4]
n = len(tab)
print(najdl_ciag(tab, n))