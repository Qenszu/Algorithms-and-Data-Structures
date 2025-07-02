from egz1btesty import runtests

"""
Zlozonosc: O(n*E)
f[i][j] - najbardziej oplacalne dotarcie do i-tej planety, majac j paliwa


Na poczatku uzupelniam pierwsza kolumne tablicy cena paliwa tankowania na 0 palencie oraz
od zapisuje cene teleportowania sie na planete (T[0][0]). Potem w petli uzupelniam funkcje i 
o minimalny koszt z:
    1. Pierwszy if:
        -tego co tam bylo
        -teleportowanie sie na T[i][0] planete
    2. Drugi if (jezeli dystans miedzy planetami + ilosc paliwa z jakimi chcemy wyladowac jest nie wiekszy od E):
        -z tego co tam bylo 
        -z wczesniejszej planety na idneksie o roznicy odleglosci (z dodaniem b, bo czasami lepiej wziasc wiecej z planety wczesniej)
    Na koncu sprawdzam czy lepiej jest doleciec z j-1 jednostkami paliwa i dotankowac jedna jednostke na planecie i   
"""

def planets( D, C, T, E ):
    n = len(D)
    f = [[float("inf") for _ in range(E+1)] for _ in range(n)]
    
    for i in range(E+1):
        f[0][i] = i * C[0]
    if T[0][0] != 0:
        f[T[0][0]][0] = T[0][1]

    for i in range(1, n):
        for b in range(E+1):
            if T[i][0] != i:
                f[T[i][0]][0] = min(T[i][1] + f[i][0], f[T[i][0]][0])
            if D[i]-D[i-1]+b < E+1:
                f[i][b] = min(f[i][b], f[i-1][D[i]-D[i-1]+b])
            f[i][b] = min(f[i][b], f[i][max(0, b-1)] + C[i])

    return f[n-1][0]


    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
