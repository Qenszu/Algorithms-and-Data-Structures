def stala_e():
    eps = 1e-10
    mianownik = 1
    a1 = (1/mianownik)
    multi = 0
    e = 0

    while a1 > eps:
        e += a1
        multi += 1
        mianownik *= multi
        a1 = (1/mianownik)
    
    return e

print(stala_e())