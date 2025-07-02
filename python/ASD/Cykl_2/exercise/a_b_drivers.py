#Jedzie A i B , szukamy najkrotszej sciezki kiedy jedzie A
#Musza sie zmieniac z kazda sciezka

import heapq
def kierowcy(G, s, t):
    n = len(G)
    distance = [float("inf") for _ in range(n)]
    distance[s] = 0
    kolejka = [(0, s, "A")]

    while len(kolejka) > 0:
        cost, u, osoba = heapq.heappop(kolejka)

        for v, w in G[u]:
            if osoba == "A":
                new_cost = cost + w
                if new_cost < distance[v]:
                    distance[v] = new_cost
                    heapq.heappush(kolejka, (new_cost, v, "B"))
            else:
                if cost < distance[v]:
                    distance[v] = cost
                    heapq.heappush(kolejka, (cost, v, "A"))

    return distance[t]

G = [[(1, 1), (2, 4)],
     [(2, 3)],
     [(1, 6)]]

print(kierowcy(G, 0, 2))
                