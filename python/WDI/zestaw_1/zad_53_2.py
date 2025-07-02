n = int(input("Podaj n: "))

liczba = 1
ilosc = 0

while liczba <= n:
    j = liczba
    while j <= n:
        k = j
        while k <= n:
            k *= 5
            ilosc += 1
        j *= 3
        ilosc += 1
    liczba *= 2
    ilosc += 1 
    
print(ilosc)
