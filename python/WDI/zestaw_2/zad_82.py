'''Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia 
dziesiętnego wartości sqrt(2). Program powinien działać poprawnie dla n < 100.'''

def ciag(x, n):
    for i in range(n):
        x2 = (1/2)(x+(2/x))
        print(x2)
        x = x2

print(ciag(2, 50))

    