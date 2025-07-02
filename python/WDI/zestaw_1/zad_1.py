from math import sqrt

n = int(input("Podaj przeciwprostokatna: "))

for a in range(1, n):
    for b in range(a, n):
        c = sqrt(a**2 + b**2)
        if c.is_integer() and c < n:
            print(a, b, int(c))

        
        