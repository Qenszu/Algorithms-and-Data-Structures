""""”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
równych sumach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool"""



def rek(T, i = 0, a = 0, b = 0, c = 0):
    size = len(T)

    if i == size:
        return a == b == c
        
    return rek(T, i+1, a + T[i], b, c) or rek(T, i+1, a, b + T[i], c) or rek(T, i+1, a, b, c + T[i])

   
