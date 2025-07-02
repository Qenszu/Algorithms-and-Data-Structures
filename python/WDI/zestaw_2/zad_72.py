end = None
def func(tab, n):
    maxi = 0
    
    for i in range(n - 1):
        k = n - 1
        j = i
        dlugosc = 0
        
        while k >= 0 and j < n:
            if tab[j] == tab[k]:
                dlugosc += 1
                j += 1
            else:
                if maxi < dlugosc:
                    maxi = dlugosc
                dlugosc = 0
                j = i           
            k -= 1   
        end
    end
        
    return maxi

#tab = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
tab = [1, 2, 3, 4, 5, 6, 7, 8, 1, 3, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(tab)
print(func(tab, n))