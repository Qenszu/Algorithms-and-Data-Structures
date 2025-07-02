x = int(input("Podaj liczbe "))

if x == 2:
    print("Jest liczba pierwsza")

elif x%2 == 0:
    print("Nie jest liczba pierwsza")
     
else:
    for i in range(3, x, 2):
        if x%i == 0:
            print("Nie jest liczba pierwsza")
            break
        else:
            print("Jest liczba pierwsza")
            break