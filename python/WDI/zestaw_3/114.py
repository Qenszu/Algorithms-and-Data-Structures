""""Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi.
Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
„szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
zwrócić położenie wież w postaci krotki (row1, col1, row2, col2).
Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
Przykładowe wywołania funkcji:
print(chess([[4,0,2],[3,0,0],[6,5,3]])) # (0,1,1,0) suma=17
print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35"""

""""Wersja z ChatGPT, moja wersja w zadaniu 111"""

""""Dla Tablicy [[4,0,2],[3,0,0],[6,5,3]] optymalnym wynikiem nie jest (0,1,1,0) suma=17 CHYBA"""


def max_rook_placement(T):
    N = len(T)
    
    # Preobliczenie sum wierszy i kolumn
    row_sums = [sum(T[i]) for i in range(N)]
    col_sums = [sum(T[j][i] for j in range(N)) for i in range(N)]
    
    max_sum = 0
    best_positions = None
    
    # Sprawdzanie wszystkich możliwych par pozycji wież
    for r1 in range(N):
        for c1 in range(N):
            for r2 in range(N):
                for c2 in range(N):
                    # Dwie wieże nie mogą stać na tym samym polu
                    if (r1 == r2 and c1 == c2):
                        continue
                    
                    # Suma pól szachowanych przez obie wieże
                    current_sum = (
                        row_sums[r1] + col_sums[c1] 
                        + row_sums[r2] + col_sums[c2]
                        - T[r1][c1] - T[r2][c2]
                    )
                    
                    # Jeśli wieże są na tej samej kolumnie/wierszu, odejmij pola podwójnie szachowane
                    if r1 == r2:
                        current_sum -= row_sums[r1]
                    if c1 == c2:
                        current_sum -= col_sums[c1]

                    # Aktualizacja maksymalnej sumy i najlepszych pozycji
                    if current_sum > max_sum:
                        max_sum = current_sum
                        best_positions = ((r1, c1), (r2, c2))
    
    return best_positions


T = [[4,0,2],
     [3,0,0],
     [6,5,3]]

print(max_rook_placement(T))