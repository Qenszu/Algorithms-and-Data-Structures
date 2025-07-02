from math import sqrt

x = int(input("x="))
i = 2 

while x != 1:
    if x%i == 0:
        print(i)
        x = x/i
    else: 
        i = i+1



