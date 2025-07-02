from egz2atesty import runtests

"""
dp[i][j] - minimalny koszt polaczenia jaki mozna uzyskac miedzy i-tym a j-tym wierzcholkiem

Algorytm rozwaza kazda pare wierzcholkow pomiedzy kotrymi jest parzysta ilosc
innych wierzcholkow. Pomiedzy tymi wierzcholkami przechodzimy petla k aby znalezc
minimalny koszt laczac kazdy wierzcholek pomiedzy z poczatkiem a reszte z koncem 
"""

def wired( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    dp = [[float("inf") for _ in range(n)] for _ in range(n)]

    for length in range(2, n + 1, 2): 
        for i in range(0, n - length + 1):  
            j = i + length - 1
            for k in range(i+1, j+1, 2):
                dp[i][j] = min(dp[i][j], 1 + abs(T[i] - T[k]) + (dp[i+1][k-1] if i + 1 < k - 1 else 0) + (dp[k + 1][j] if k + 1 < j else 0))

    return dp[0][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )