from queue import PriorityQueue

def dijkstra(G, start):
    #relaxation
    def relaxation(v,u,weight):
        if(dist[u]>dist[v]+weight):
            dist[u]=dist[v]+weight
            return True
        return False

    n = len(G)
    dist = [float('inf') for _ in range(n)]

    q = PriorityQueue()
    q.put((0,start))
    dist[start]=0
    
    while not q.empty():
        cost, v = q.get()
        for u,weight in G[v]:
            if(relaxation(v,u,weight)):
                q.put((dist[u],u))
    print(dist)
graf = [[(1,3),(3,4)],[(2,5)],[],[(2,7)]]
dijkstra(graf,0)