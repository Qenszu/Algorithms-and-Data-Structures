""""Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A
cyfr 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
ilość wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszy
bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
10010(2), 10100(2), 11000(2)"""

def Is_Prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1

    return True


def rek(A, B, liczba = 0, m = 1):
    if A == 1 and B == 0:
        liczba += m
        if not Is_Prime(liczba):
            return 1
        else:
            return 0
    result = 0

    if B > 0:
        result += rek(A, B - 1, liczba, m*2)  
    if A > 1:
        result += rek(A-1, B, liczba + m, m*2)
    
    return result

    
    
print(rek(2, 3))
    