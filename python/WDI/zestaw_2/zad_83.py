end = None

def func(tab):
    size = len(tab)
    maxi = 0
    dl = 0
    
    for i in range(size - 2):
        a1 = tab[i][0]
        b1 = tab[i][1]
        a2 = tab[i+1][0]
        b2 = tab[i+1][1]
        a3 = tab[i+2][0]
        b3 = tab[i+2][1]

        if  a1*a3*b2*b2 == a2*a2*b1*b3:
            dl += 1
        else:
            if maxi < dl:
                maxi = dl
                print(maxi)
                dl = 0
        if maxi < dl:
            maxi = dl
    end
    if maxi == 0:
        return 0
    return maxi + 2

tab = [(1, 2), (1, 4), (1, 8), (1, 16), (1, 32), (1, 64)]

print(func(tab))
        
            