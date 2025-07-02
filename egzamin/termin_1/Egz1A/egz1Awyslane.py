from egz1Atesty import runtests
"""
Patryk Opala
Moj kod laczy tablice K i R po czym ja sortuje
Modifikuje tablice P tak aby byla to tablica krotek gdzie kazda krotka do odleglosc
procesora a druga to wrtosc True ktora oznacza ze w dany procesor moge strzelic z katapulty
Nastepnie w petli ide od konca tablicy K (czyli od najdalszej katapulty) i strzelam do najblizszego 
mozliwego procesora po czym zwiekszam licznik i przerywam petle po czym przechodze do kolejnej katapulty
na koncu zwracam licznik
zlozonosc O((n+m)^2)
"""

def battle(P, K, R):
    size_P = len(P)
    size_K = len(K)

    for i in range(size_K):
        K[i] = (K[i], R[i])

    for i in range(size_P):
        P[i] = (P[i], True)

    P.sort()
    K.sort()
    cnt = 0

    for i in range(size_K - 1, -1, -1):
        for j in range(size_P):
            if P[j][0] > K[i][0]:
                if P[j][1] == True and P[j][0] <= K[i][0] + K[i][1]:
                    P[j] = (P[j][0], False)
                    cnt += 1
                    break


    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )

