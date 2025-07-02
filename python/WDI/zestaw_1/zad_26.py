from math import sqrt
def rozwiniecie(a, b, n):

    #czesc przed przecinkiem
    print(a//b, end='.')
    reszta = a%b

    #ilosc liczb po przecinku
    for i in range(n):
        reszta *= 10
        print(reszta//b, end='')
        reszta %= b

rozwiniecie(99,70,99,)
print("\n", sqrt(2))
