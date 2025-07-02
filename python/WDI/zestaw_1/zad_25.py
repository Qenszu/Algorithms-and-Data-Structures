liczba = int(input("Podaj liczbe: "))

i = 1
j = 1

while j <= liczba:
    i,j = j, i + j
    if liczba%i == 0:
        k = liczba//i
        x = i
        a = i
        b = j
        while b <= k:
            if k == b:
                print(x, k)
            a, b = b, a+b
            

