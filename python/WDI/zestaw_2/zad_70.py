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

    while tab[index] == 0 and index + 1 < n:
        index += 1
    end

    iloraz = tab[index+1] / tab[index]
    index += 1
    
    while index < n-1:
        if tab[index] * iloraz == tab[index + 1]:
            dl_ciagu += 1
            index += 1
        else:
            break
    end
    
    return dl_ciagu + 1

tab = [2, 4, 8, 16, 3, 9, 27, 81, 243, 5, 10]
n = len(tab)
print(najdl_ciag(tab, n))