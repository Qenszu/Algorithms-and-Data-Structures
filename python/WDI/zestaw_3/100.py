""""Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu."""

def main_func(T, k):
    size = len(T)

    for a in range(3, size + 1, 2): #sprawdzamy kwadraty o boku (3, 5, 7, ...)
        for i in range(size - a + 1):
            for j in range(size - a + 1):
                
                if T[i][j]*T[i+a-1][j]*T[i][j+a-1]*T[i+a-1][j+a-1] == k:
                    print(f"Bok {a}, wiersz {i + (a//2) + 1}, kolumna {j + (a//2) + 1}")


T = [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 6],
     [1, 1, 1, 1, 1],
     [1, 1, 3, 1, 2]]

main_func(T, 36)
                

