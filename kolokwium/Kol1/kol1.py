# Patryk Opala 425567
#Program wykorzystuje algorytm sortowania typu bucket sort ktory polega na 
#rozlozeniu elemetow tablicy do "kubelkow" (przedzialow) ktore potem za
#pomoca funkcji insertion_sort zostana posortowane, po czym "kubelki"
#zostana zlaczone w jedna calosc i zwrocone.
#Dzieki posiadaniu posortowanej tablicy moge przejsc po niej 
#i znalezc liniowo elementy odlegle o conajmniej D i zliczac
#te przypadki, na koncu je zwracam i to koniec
#PS. w moim kodzie nie wykorzystuje zmniennej M 
#Zlozonosc czasowa: O(n) --> korzystam z liniowego bucket sorta oraz liniowo porownuje elementy w fun ogrodzenie
#Zlozonosc pamieciowa: O(n) --> tworze nowa tablice result w funkcji bucket sort

from kol1testy import runtests

def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    j = i - 1
    key = A[i]
    while j >= 0 and key < A[j]:
      A[j+1] = A[j]
      j -= 1

    A[j+1] = key

def bucket_sort(T):
  n = len(T)
  maxi = max(T)
  mini = min(T)
  bucket_range = ((maxi-mini)/n)
  buckets = [[] for _ in range(n)]

  for num in T:
    ind = int((num-mini)/bucket_range)
    if ind == n:
      ind -= 1

    buckets[ind].append(num)

  result = []
  for bucket in buckets:
    insertion_sort(bucket)
    result.extend(bucket)

  return result

def ogrodzenie(M, D, T):
  T = bucket_sort(T)
  n = len(T)
  cnt = 0

  for i in range(n-1):
    if T[i+1] - T[i] >= D:
      cnt += 1

  return cnt  
  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )


