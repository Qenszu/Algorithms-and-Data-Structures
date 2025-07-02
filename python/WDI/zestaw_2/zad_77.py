end = None
def func(tab, n):
    maxi = 0
    
    for i in range(n - 1):
        k = n - 1
        j = i
        dlugosc = 0
        
        while j <= k:
            if tab[j]%2 != 0 and tab[j] == tab[k]:
                dlugosc += 1
                j += 1
            if maxi < dlugosc and abs(j - k) < 2:
                maxi = dlugosc
            if tab[j]%2 == 0:
                dlugosc = 0
            k -= 1   
        end
    end
    
    if maxi > 1:
        return maxi - 1
    else:
        return maxi

#tab = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
tab = [1, 3, 2, 3, 1, 5, 6, 7, 1, 2, 3, 4, 4, 3, 2, 1]
#tab = [1, 2, 4]
n = len(tab)
print(func(tab, n))