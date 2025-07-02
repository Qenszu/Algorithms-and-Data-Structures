x = int(input("Podaj liczbe: "))

a = 1
b = 1
z = 0

while a < x:
    if a*b == x:
        print("Ta liczba jest iloczynem dwoch kolejnych wyrazow ciagu fibiego")
        print(a, b)
        z = 1
        break
    else:
        a, b = b, a+b
if z == 0:
    print("Ni mo")