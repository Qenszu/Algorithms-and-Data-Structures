liczba = int(input("Podaj liczbe: "))

def odwracanie_liczb(x):
    y = 0
    while x//10 != 0:
        y *= 10
        y += x%10
        x //= 10

    y *= 10
    y += x

    return y


        