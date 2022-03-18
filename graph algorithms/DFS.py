# zlożonośc : O(V + E) - musi odwiedzic wszystkie wierzcholki i krawedzie

def DFS(G):
    def DFSVisit(G,u):
        nonlocal time
        '''time += 1 # czas odwiedzenia, zapisuje od poczatku
        d[u] = time # zapis czasu odwiedzenia'''
        visited[u] = True
        #print(u,time,end=" -> ")
        for p in G[u]:
            if visited[p] is False:
                parent[p] = u
                DFSVisit(G, p)

        time += 1 # czas przetwarzania, zapisuje od konca
        d[u] = time # zapis czasu przetworzenia

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [-1 for _ in range(n)]
    time = 0
    for i in range(n):
        if visited[i] is False:
            DFSVisit(G,i)

    return visited,parent,d

T = [
    [1,2],
    [0,3,4],
    [0,4],
    [1,5],
    [1,2,5],
    [3,4],
]