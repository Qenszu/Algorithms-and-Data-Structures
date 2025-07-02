""""W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy
króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest
globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik
ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do
prawego dolnego narożnika."""

from math import log10

def last_smaller_than_first(num1, num2):
    num2_size = int(log10(num2)) + 1

    return num2//10**(num2_size - 1) > num1%10
    

def rek(T, w = 0, k = 0):
    if w == k == 7:
        return True
    
    if w < 7:
        if last_smaller_than_first(T[w][k], T[w+1][k]):
            if rek(T, w + 1, k):
                return True
    if k < 7:
        if last_smaller_than_first(T[w][k], T[w][k+1]):
            if rek(T, w, k + 1):
                return True
    if k < 7 and w < 7:
        if last_smaller_than_first(T[w][k], T[w+1][k+1]):
            if rek(rek(T, w + 1, k + 1)):
                return True
    
    return False

T = [
    [99, 12, 12, 12, 12, 12, 12, 12],
    [91, 91, 91, 91, 91, 91, 91, 12],
    [91, 91, 91, 91, 91, 91, 91, 12],
    [91, 91, 91, 91, 91, 91, 91, 12],
    [91, 91, 91, 91, 91, 91, 91, 12],
    [91, 91, 91, 91, 91, 91, 91, 12],
    [91, 91, 91, 91, 91, 91, 91, 12],
    [91, 91, 91, 91, 91, 91, 91, 78]
]

print(last_smaller_than_first(91, 91))
print(rek(T))