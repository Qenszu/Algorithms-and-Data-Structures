year = 2024
wynik_x = 1
wynik_y = 2023

def chec_fib(x, y):
    while x < year:
        x, y = y, y+x
        if y == year:
            return 1

for suma in  range(2, year):
    for x in range(1, suma):
        y = suma-x
        if chec_fib(x, y):
            if wynik_y + wynik_x > y + x:
                wynik_x = x
                wynik_y = y

print(wynik_x, wynik_y)

