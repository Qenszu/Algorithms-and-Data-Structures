def NWW(a, b):
    if a < b:
        a, b = b, a
    for i in range(a, a*b, a):
        if i%b == 0:
            return i
    else: 
        return a*b
        
x = int(input("Podaj 1 cyfre: "))
y = int(input("Podaj 2 cyfre: "))
z = int(input("Podaj 3 cyfre: "))

print(NWW(NWW(x, y), z))
