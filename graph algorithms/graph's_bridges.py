from math import inf

def DFS(G):
    def DFSVisit(G,u):
        nonlocal time
        time += 1 # czas odwiedzenia, zapisuje od poczatku
        d[u] = time # zapis czasu odwiedzenia'''
        visited[u] = True
        low[u] = d[u]
        for p in G[u]:
            if visited[p] is False:
                parent[p] = u
                DFSVisit(G, p)
                low[u] = min(low[u],low[p])
            elif parent[u] != p:
                low[u] = min(low[u],d[p])
        if d[u] == low[u] and parent[u] is not None:
            print(u,parent[u])

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [-1 for _ in range(n)]
    low = [inf for _ in range(n)]
    time = 0
    for i in range(n):
        if visited[i] is False:
            DFSVisit(G,i)

    return

# G = [
#     [1,3],
#     [0,2],
#     [1,3,5],
#     [0,2,4],
#     [3],
#     [2,6,7],
#     [5,7],
#     [6,5],
# ]
#
# K = [
#     [1,6],
#     [0,2],
#     [1,3,6],
#     [2,4,5],
#     [3,5],
#     [3,4],
#     [0,2,7],
#     [6],
# ]

K = [
    [1,2],
    [0,2],
    [1,0,3],
    [2,7,4],
    [3,5,6],
    [4,6],
    [4,5],
    [3,8,9],
    [7,9],
    [7,8],
]
print(DFS(K))





