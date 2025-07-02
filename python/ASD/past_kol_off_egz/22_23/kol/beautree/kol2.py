from kol2testy import runtests

def beautree(G):
    n = len(G)

    def find(v):
        if v != parent[v]:
            parent[v] = find(parent[v])
        return parent[v]
    
    edges = []
    for v in range(n):
        for u, w in G[v]:
            if v < u:
                edges.append((w, v, u))
    
    edges.sort(key=lambda x: x[0])
    for i in range(len(edges) - (n-1)):
        cnt = 0
        parent = [i for i in range(n)]
        rank = [0] * n
        #print(edges[i:(n-1+i)]) 
        for weight, v, u in edges[i:(n-1+i)]:
            v = find(v)
            u = find(u)

            if v == u:
                cnt = 0
                break

            if rank[v] < rank[u]:
                parent[v] = u
            else:
                parent[u] = v
                if rank[v] == rank[u]:
                    rank[v] += 1
            cnt += weight
        if cnt != 0:
            break
            

    return cnt if cnt != 0 else None


G = [ [(1,3), (2,1), (4,2)], # 0
[(0,3), (2,5) ], # 1




[(1,5), (0,1), (3,6)], # 2
[(2,6), (4,4) ], # 3
[(3,4), (0,2) ] ]
#print(beautree(G))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)