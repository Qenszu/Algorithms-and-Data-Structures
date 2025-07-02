from zadtesty import runtests
from queue import PriorityQueue

"""
Algorytm to Dijsktra ktora w kolejce przechowywuje czas w jakim dostajemy sie do wierzcholka, 
wierzcholek, oraz ilosc jednostek czasu z jakimi rycerz trafia do danego wierzcholka od ostatniego snu
(inaczej ile rycerz juz nie spi), w relaksacji rozwazam dwa przypadki:
  1. gdy rycerz trafi do wierzcholka beda obudzony wiecej niz 16h, wtedy do przejscia 
     doliczamy 8h ktore spedzil na snie w poprzednim wiercholku
  
  2. gdy rycerz moze dostac sie do wierzcholka bedac obudzony nie wiecej niz 16h

Na koncu zwracamy minimalny czas dotarcia do wierzcholka
"""

def goodknight( G, s, t ):
  n = len(G)
  dist = [float("inf")] * n
  dist[s] = 0
  q = PriorityQueue()
  
  g = [[] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if G[i][j] != -1:
        g[i].append((j, G[i][j]))
  G = g
  q.put((0, s, 0))

  while not q.empty():
    time, v, awake = q.get()
    for u, d in G[v]:
      if awake + d > 16:
        if dist[u] > dist[v] + d + 8:
          dist[u] = dist[v] + d + 8
          q.put((dist[u], u, d))
      else:
        if dist[u] > dist[v] + d:
          dist[u] = dist[v] + d
          q.put((dist[u], u, awake + d))
        

  return dist[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
