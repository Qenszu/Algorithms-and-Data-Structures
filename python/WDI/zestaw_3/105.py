""""Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę
jedynek, np. 22 = 101102 i 14 = 11102. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2¿N1. Proszę napisać
funkcję, która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba
zgodnych elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne
tablice powinny pozostać nie zmieniane."""

def zgodne(a, b):
    suma = 0

    while a != 0:
        suma += a%2
        a //= 2

    while b != 0:
        suma -= b%2
        b //= 2

    if suma == 0: 
        return True

    return False

def main_func(T1, T2):
    size_1 = len(T1)
    size_2 = len(T2)

    for i in range(size_2 - size_1 + 1):
        for j in range(size_2 - size_1 + 1):
            licz = 0

            for a in range(size_1):
                for b in range(size_1):
                    if zgodne(T1[a][b], T2[a+i][b+j]):
                        licz += 1
                    if licz/(size_1*size_1) > (1/3):
                        return True
                #end for
            #end for
        #end for
    #end for

    return False

T1 = [[2,2],
      [2, 2]]

T2 = [[3, 3, 1],
      [3, 1, 3],
      [3, 3, 1]]

print(main_func(T1, T2))