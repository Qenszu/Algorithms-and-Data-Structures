def NWD(a, b):
    while b != 0:
        if a < b:
            a, b = b, a
        pom = a%b
        a = b
        b = pom
    return a

x = int(input("Podaj 1 cyfre: "))
y = int(input("Podaj 2 cyfre: "))
z = int(input("Podaj 3 cyfre: "))

print(NWD(NWD(x, y), z))