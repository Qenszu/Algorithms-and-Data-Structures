from kol2testy import runtests
from queue import PriorityQueue

"""
dist[i][j] - minimalny czas dotarcia do wierzcholka i z j iloscia nieprzespanych
jednostek czasu

Zadanie polega na zmodyfikowaniu algorytmu Dijsktry by szukala
najmniejsza ilosc czasu potrzebna by przejsc do danego wierzcholka
z x iloscia nieprzespanych godzin
"""

def warrior( G, s, t):
  n = 0
  for v, u, w in G:
    n = max(n, max(v, u))
  n += 1

  g = [[] for _ in range(n)]

  for v, u, w in G:
    g[v].append((u, w))
    g[u].append((v, w))

  dist = [[float("inf") for i in range(17)] for j in range(n)]
  for i in range(17):
    dist[s][i] = 0
  q = PriorityQueue()
  q.put((0, s, 0))

  while not q.empty():
    d, v, awake = q.get()

    for u, time in g[v]:
      
      if awake + time > 16:
        if dist[u][time] > dist[v][awake] + time + 8:
          dist[u][time] = dist[v][awake] + time + 8
          q.put((dist[u][time], u, time))
      
      else:
        if dist[u][time+awake] > dist[v][awake] + time:
          dist[u][time+awake] = dist[v][awake] + time
          q.put((dist[u][time+awake], u, time+awake))
        
        if dist[u][time] > dist[v][awake] + time + 8:
          dist[u][time] = dist[v][awake] + time + 8
          q.put((dist[u][time], u, time))

  return min(dist[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )