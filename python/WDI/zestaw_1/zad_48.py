end = None
def IsPrime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    end
    return True



def func(n):
    x = 1
    while True:
        pom = x
        pom2 = x//10
        wynik = 0
        if IsPrime(x):
            while pom != 0:
                if pom%10 < pom2%10 and pom > 9:
                    wynik = 0
                    x += 2
                    break
                else:
                    wynik += pom%10
                    wynik *= 10
                    pom = pom2
                    pom2 //= 10
                    #print(pom)
            if wynik//10 == n:
                return x
                break
            else:
                x += 2
                #print(x)

print(func(101))