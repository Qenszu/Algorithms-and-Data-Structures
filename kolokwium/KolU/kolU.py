from kolUtesty import runtests

""""
Zlozonosc O(n*k)
Algorytm idac po tablicy T zlicza ilosc wystapien kwiatow i zapisuje je
do tablicy K po czym dla tego samego n zlicza ilosc kaktusow z wieksza liczba kwiatkow 
ktore pojawily sie w tablicy T przed n - tym elementem
"""

def kawa(T, k):
  # tu prosze wpisac wlasna implementacje

  K = [0 for _ in range(k+1)]
  n = len(T)
  cnt = 0

  for i in range(n):
    K[T[i]] += 1
    for j in range(T[i]+1, k+1):
      cnt += K[j]

  return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kawa, all_tests = True )

