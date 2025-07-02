n = int(input("Podaj n: "))
a = 1
index = 1
x = 0

while a <= n:
    a = index * index + index + 1
    index += 1
    if n%a == 0:
        print("TAK")
        x = 1
        break
    

if x == 0:
    print("NIE")
