n = int(input("Podaj n: "))
ilosc = 1

for i  in range(1, n):
    x = i
    while x%2 == 0:
        x //= 2
    while x%3 == 0:
        x //= 3
    while x%5 == 0:
        x //= 5
    if x == 1:
        ilosc += 1 

print(ilosc)
        