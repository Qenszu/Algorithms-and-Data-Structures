from egz1Btesty import runtests
from queue import Queue

"""
Patryk Opala
W swoim algorytmie tworze liste sasiedztwa po czym implementuje najzwyklejszego bfs ktory omija zadana 
w parametrach funkcji sciezke miedzy a i b
Nastepnie w petli przechodze po kazdej kazdej sciezce (zadanej jako x i y) i sprawdzam czy mozliwe jest 
przejscie z wierzcholka x do y ale nie przechodza po bezposredniej sciezce x --> y
Zlozonosc: E razy odpalam bfs(V+E) czyli O(VE + E^2)
"""

def critical_1(V, E):

    G = [[] for _ in range(V)]

    for v, u in E:
        G[v].append(u)


    def bfs(G, s, a, b, V):
        q = Queue()
        q.put(s)
        visited = [False for _ in range(V)] 
        visited[s] = True

        while not q.empty():
            v = q.get()

            for u in G[v]:
                if a != v or u != b:
                    if not visited[u]:
                        visited[u] = True
                        q.put(u)
        
        return visited

    cnt = 0
    for x, y in E:
        v = bfs(G, x, x, y, V)
        if not v[y]:
            cnt += 1



    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical_1, all_tests = True)

V = 4
E = [(0, 1), (0,2),  (0, 3), (1,2), (1,3), (2,3)]
#print(critical_1(V, E))
#print(critical_2(V, E))

