""""Patryk Opala
1. Moj algorytm zlicza ilosc wierzcholkow
2. Tworze tablice visited aby pozniej sprawdzac ktore osrodki zostaly juz odwiedzone 
    przez co potem w algorytmie dijkstry nie przechodze przez ten wierzcholek 
3. Tworze graf w reprezentacji listy sasiedztwa z podwojonymi wartosciami krawedzi
4. Tworze petle for ktora uruchamia sie R razy i wywoluje algorymt dijkstry
5. Algorytm dijsktry sprawdza czy moge przejsc przez dany weirzcholek, jezeli tak to ustwiam odleglosci
6. Na koncu sprawdzam do ktrego osrodka mam najkrotsza droge, zliczam te droge i ustawiam mu visited na True
7. Do result dodaje te droge
8. Powtarzam algorymt z wylaczeniem odwiedzonych osrodkow"""


from kol2testy import runtests
from queue import PriorityQueue

def lets_roll(start_city, flights, resorts):
    n_res = len(resorts)
    resorts.sort()
    n_fli = len(flights)
    n = 0
    for i in range(n_fli):
        n = max(n, max(flights[i][0], flights[i][1]))
    n += 1 

    G = [[] for i in range(n)]
    for i in range(n_fli):
        G[flights[i][0]].append((flights[i][1], flights[i][2]*2))
        G[flights[i][1]].append((flights[i][0], flights[i][2]*2))

    result = 0
    q = PriorityQueue()

    dist = [float("inf") for _ in range(n)]
    dist[start_city] = 0
    visited = [-1 for _ in range(n)]
    for i in resorts:
        visited[i] = 0
    q.put((0, start_city))

    while not q.empty():
        d, v = q.get()

        for u, time in G[v]:
            if visited[u] == -1:
                if dist[u] > dist[v] + time:
                    dist[u] = dist[v] + time
                    q.put((dist[u], u))
            else:
                if dist[u] > dist[v] + time:
                    dist[u] = dist[v] + time
                    visited[u] = 1 
    for x in resorts:
        if dist[x] != float("inf"):
            result += dist[x]  
        
    return result

flights = [(0, 1, 2), (0, 2, 4), (0, 3, 8), (3, 4, 16), (1, 4, 1), (2, 4, 1)]
r = [1, 2, 4]
#print(lets_roll(0, flights, r))


runtests(lets_roll, all_tests = True)
