#Kacper Feliks

#moj algorytm to przerobiona dijkstra która rozważa każdy wieżchołek z możliwością spania lub nie
#na początku zamienia graf na listę sąsiedstwa
#następnie rozpatruje każdy wieżchołek z możliwościa spania lub nie jak w zwykłej dijkstrze
#jak również wszystkie wieżchołki do których da się dostać z mniejszą ilością nie przespanych godzin niż najkrótrzą ścieżką

#złożonosć O(ElogV) jak dijkstry bo tworzenie listy sąsiedstwa O(E)
from kol2testy import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance_sleep = [float("inf") for _ in range(n)]
    distance_not_sleep= [float("inf") for _ in range(n)]
    distance[s] = 0
    distance_sleep[s] = 0
    distance_not_sleep[s] = 0
    time = 0
    Q = PriorityQueue()
    Q.put((0, s, time))

    while not Q.empty():

        (cur_distance, v,time) = Q.get()
        if cur_distance > distance[v] and cur_distance > distance_sleep[v]: continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight
            if dist+8 < distance_sleep[v_son] and time+weight<=16: #spanie w v_son
                distance_sleep[v_son]= dist+8
                Q.put((dist + 8, v_son,0))
            
            if distance_not_sleep[v_son] > time + weight and dist < distance_sleep[v_son] and time+weight<=16: #spanie nie optymalnie ale w v_son mamy mniej nie przespanych godzin
                distance_not_sleep[v_son]=time+weight
                Q.put((dist, v_son,time + weight))

            if dist < distance[v_son] and time+weight<=16: #nie spanie w v_son
                distance[v_son] = dist
                distance_not_sleep[v_son]=time + weight
                Q.put((dist, v_son,time + weight))


    print(distance, distance_sleep)
    return min(distance[e],distance_sleep[e])


def warrior( G, s, t):
  n=0
  for u,v,w in G:
    n=max(n,u,v)
  G_son=[[] for _ in range(n+1)]
  for u,v,weight in G:
      G_son[u].append((v,weight))
      G_son[v].append((u,weight))

      
  return dijkstra(G_son,s,t)

G = [(0, 9, 6), (0, 35, 14), (0, 72, 11), (0, 87, 14), (0, 92, 5), (1, 7, 12), (1, 11, 16), (1, 44, 6), (1, 52, 8), (1, 81, 4), (1, 82, 10), (1, 84, 15), (2, 61, 6), (2, 64, 8), (2, 69, 10), (2, 71, 11), (2, 75, 14), (2, 93, 6), (3, 22, 14), (3, 43, 16), (4, 6, 5), (4, 32, 12), (4, 51, 11), (4, 60, 16), (4, 90, 4), (5, 22, 11), (5, 39, 16), (5, 54, 6), (5, 91, 11), (5, 97, 14), (5, 98, 14), (6, 10, 14), (6, 19, 14), (6, 60, 14), (6, 65, 2), (6, 90, 4), (6, 99, 6), (7, 11, 4), (7, 17, 8), (7, 23, 16), (7, 25, 16), (7, 44, 15), (7, 70, 6), (7, 77, 14), (7, 81, 12), (8, 16, 16), (8, 59, 14), (9, 21, 11), (9, 31, 16), (9, 67, 12), (9, 72, 6), (9, 92, 11), (10, 19, 2), (10, 48, 16), (10, 60, 16), (10, 65, 15), (10, 79, 11), (10, 80, 11), (10, 89, 10), (10, 90, 16), (10, 99, 11), (11, 17, 4), (11, 40, 11), (11, 70, 10), (11, 81, 16), (12, 26, 4), (12, 83, 6), (12, 96, 16), (13, 23, 8), (13, 40, 15), (13, 77, 8), (14, 31, 14), (14, 35, 6), (14, 36, 11), (14, 56, 16), (14, 67, 11), (14, 87, 14), (15, 28, 2), (16, 31, 8), (16, 35, 14), (16, 56, 8), (16, 58, 12), (16, 59, 2), (17, 23, 8), (17, 25, 16), (17, 40, 8), (17, 70, 14), (17, 77, 8), (18, 26, 8), (18, 83, 11), (19, 32, 10), (19, 48, 14), (19, 53, 4), (19, 65, 14), (19, 79, 11), (19, 80, 8), (19, 89, 8), (19, 99, 12), (20, 22, 16), (20, 61, 6), (20, 75, 11), (20, 93, 14), (21, 36, 14), (21, 72, 10), (21, 79, 14), (21, 87, 4), (22, 39, 8), (22, 54, 8), (23, 40, 6), (23, 68, 14), (23, 77, 8), (24, 69, 11), (24, 78, 8), (25, 27, 16), (25, 29, 5), (25, 68, 14), (25, 77, 11), (26, 46, 16), (26, 73, 14), (26, 83, 6), (27, 29, 12), (29, 66, 14), (29, 77, 16), (29, 98, 14), (30, 34, 1), (30, 58, 8), (30, 60, 8), (30, 99, 15), (31, 35, 8), (31, 56, 2), (31, 58, 11), (31, 59, 11), (31, 67, 8), (31, 72, 14), (32, 50, 11), (32, 51, 10), (32, 63, 11), (32, 65, 6), (32, 80, 8), (32, 89, 14), (32, 90, 12), (32, 99, 11), (33, 45, 12), (33, 50, 14), (33, 51, 8), (33, 57, 12), (33, 62, 6), (33, 63, 5), (33, 65, 14), (33, 80, 14), (34, 60, 8), (34, 99, 15), (35, 36, 15), (35, 56, 11), (35, 59, 16), (35, 67, 5), (35, 72, 8), (36, 49, 14), (36, 72, 14), (36, 88, 12), (36, 92, 4), (36, 94, 16), (37, 74, 2), (37, 91, 16), (37, 97, 16), (38, 41, 2), (38, 57, 10), (38, 62, 11), (38, 76, 11), (39, 54, 10), (39, 74, 11), (39, 75, 16), (39, 91, 11), (39, 97, 14), (40, 77, 14), (41, 55, 5), (41, 57, 8), (41, 62, 11), (41, 63, 16), (41, 76, 11), (42, 48, 5), (42, 79, 11), (42, 87, 14), (42, 89, 10), (43, 78, 2), (44, 52, 4), (44, 70, 11), (44, 81, 2), (44, 84, 16), (45, 51, 12), (45, 62, 14), (45, 76, 14), (45, 83, 12), (45, 86, 14), (46, 86, 16), (48, 53, 15), (48, 63, 15), (48, 79, 11), (48, 80, 8), (48, 89, 6), (49, 67, 14), (49, 88, 10), (50, 86, 16), (50, 90, 8), (50, 99, 14), (51, 65, 8), (51, 90, 14), (52, 70, 14), (52, 84, 14), (53, 79, 8), (53, 89, 8), (53, 99, 14), (54, 97, 10), (55, 57, 14), (55, 95, 16), (56, 58, 8), (56, 59, 11), (56, 67, 11), (56, 72, 16), (57, 62, 6), (58, 59, 14), (59, 67, 12), (60, 99, 8), (61, 64, 2), (61, 69, 16), (61, 71, 8), (61, 74, 15), (61, 75, 8), (61, 93, 8), (62, 63, 6), (62, 80, 16), (63, 65, 16), (63, 76, 6), (63, 89, 16), (64, 71, 6), (64, 93, 8), (65, 80, 15), (65, 90, 6), (65, 99, 8), (66, 82, 12), (66, 85, 2), (66, 98, 8), (67, 72, 14), (67, 94, 15), (69, 93, 12), (70, 81, 8), (70, 82, 11), (71, 75, 8), (71, 93, 8), (72, 79, 14), (72, 87, 11), (72, 92, 16), (73, 95, 8), (74, 75, 8), (79, 87, 11), (79, 89, 8), (80, 89, 6), (81, 82, 14), (82, 84, 12), (82, 85, 10), (85, 98, 11), (88, 92, 12), (90, 97, 15), (90, 99, 6), (91, 97, 4)]
print(warrior(G, 0, 4))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( warrior, all_tests = True ) 