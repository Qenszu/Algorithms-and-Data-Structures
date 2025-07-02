
def E_pom():
    e = 1
    w = 1 
    n = 2

    while w != 0:
        e += w
        w /= n
        n += 1
    #end while

    print(e)

#E_pom()

def E(x):
    tab = [0 for a in range(x)]
    czesc_calkowita = 1
    
    w = 1
    n = 1

    while w != 0:
        czesc_calkowita += w//n
        reszta = w%n
        
        for i in range(x):
            reszta *= 10
            tab[i] += reszta // n
            reszta %= n
        #end for

        w /= n
        n += 1
    #end while

    for j in range(x - 1, -1, -1):
        tab[j - 1] += tab[j]//10
        tab[j] = tab[j]%10
    #end for


    print(int(czesc_calkowita), end = '.')
    for b in range(x):
        print(int(tab[b]), end = '')

E(100)
