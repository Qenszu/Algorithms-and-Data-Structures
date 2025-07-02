from math import sqrt



for z in range(2, 1000000, 2):
    suma = 0
    for i in range(1, int(sqrt(z))+1):
        if z%i == 0:
            if i == z//i:
                suma += i
            else:
                suma = suma + i + (z//i)
    if suma-z == z:
        print(z, suma-z)

