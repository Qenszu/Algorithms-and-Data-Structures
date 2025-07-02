
x = int(input("Podaj liczbe: "))
suma = 0 #suma
n = 0 #ilosc przejsc
i = 1 #liczba nieparzysta

while suma<=x:
    suma += i
    n += 1
    i += 2
print(n-1)

