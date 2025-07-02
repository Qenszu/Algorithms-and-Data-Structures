from math import sqrt

def suma_dzielnikow(x):
    suma = 0
    for i in range(2, int(sqrt(x)+1)):
        if x%i == 0:
            if i != x/i:
                suma += i + x/i
            else:
                suma += i
    return int(suma + 1)
a = 1
while a < 1000000:
    b = suma_dzielnikow(a)
    if b > 10000000:
        break
    elif suma_dzielnikow(b) == a and a != b:
        print("Te cyfry sa zaprzyjaznione ", a, b)
        a = b + 1
    else:
        a += 1
print("KONIEC")
