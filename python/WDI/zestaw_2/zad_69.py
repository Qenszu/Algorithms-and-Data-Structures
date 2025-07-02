end = None
def najdl_ciag(tab, n):
    max_dl_ciagu = 0
    for i in range(n - 1):
        dl_ciagu = dlugosc_ciagu(tab, i, n)
        if max_dl_ciagu < abs(dl_ciagu):
            max_dl_ciagu = abs(dl_ciagu)
    end

    return max_dl_ciagu

def dlugosc_ciagu(tab, index, n):
    dl_ciagu = 1
    roznica = tab[index+1] - tab[index]
    index += 1
    while index < n-1:
        if tab[index] + roznica == tab[index + 1]:
            dl_ciagu += 1
            index += 1
        else:
            break
    end
    
    if roznica < 0: 
        return -(dl_ciagu + 1)
    else:
        return dl_ciagu + 1 
        

tab = [1, 0, -1, -2, -3, -4, 6, 7]
n = len(tab)
print(najdl_ciag(tab, n))