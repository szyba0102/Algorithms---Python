'''Sortowanie topologiczne - kolejnosc zadan
Sortowanie topologiczne w DAGu (grafie acyklicznym) poleg ana ułożeniu wierzchołków
w takiej kolejności, że krawędzie wskazują tylko "z lewej na prawą"
wykorzytsanie DFS, A ---> B oznacza ze B ma byc wykonane przed A
ZŁOŻONOŚĆ: O(V+E)'''
def DFS(G):
    def DFSVisit(G,u):
        nonlocal time
        visited[u] = True
        #print(u,time,end=" -> ")
        for p in G[u]:
            if visited[p] is False:
                parent[p] = u
                DFSVisit(G, p)
        list.append(u)
        '''time += 1 # czas przetwarzania, zapisuje od konca
        d[u] = time # zapis czasu przetworzenia'''

    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [-1 for _ in range(n)]
    list = []
    time = 0
    for i in range(n):
        if visited[i] is False:
            DFSVisit(G,i)

    return list[::-1]


D = [
    [1],
    [2],
    [3,4,5],
    [],
    [],
    [],
    [2,7],
    [],
    [6,7],
]

print(DFS(D))