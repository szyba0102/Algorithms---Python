'''Dwa razy użyty DFS. Dobre rozwiązanie'''
def DFS(G):
    def DFSVisit(G,u):
        nonlocal time
        visited[u] = True

        for p in G[u]:
            if visited[p] is False:
                DFSVisit(G, p)

        time += 1 # czas przetwarzania, zapisuje od konca
        d[u][1] = time # zapis czasu przetworzenia

    n = len(G)
    visited = [False for _ in range(n)]
    d = [[i,-1] for i in range(n)]
    l = []
    time = 0
    for i in range(n):
        if visited[i] is False:
            DFSVisit(G,i)

    return d

def DFS2(G,K):
    def DFSVisit(G,u,inx):
        visited[u] = True

        for p in G[u]:
            if visited[p] is False:
                DFSVisit(G, p,inx)

        list[inx].append(u)

    n = len(G)
    visited = [False for _ in range(n)]
    list = []
    inx = 0
    for i in range(n):
        if visited[K[i][0]] is False:
            list.append([])
            DFSVisit(G,K[i][0],inx)
            inx += 1
    return list

def SSK(A):
    n = len(A)
    K= DFS(A)   # czasy przetworzenia wierzchołków

    K.sort(key=lambda x: x[1], reverse=True)
    #print(K)
    N = [[] for _ in range(n)]
    for i in range(n):  # odwrócenie krawędzi w grafie (stworzenie nowego grafu)
        for j in A[i]:
            N[j].append(i)
    print(N)
    l = DFS2(N,K)   # drugi DFS idący zgodnie z malejącym czasem przetwoerzenia wierchołków
    return l


D = [
    [2],   # 0
    [0,3],  # 1
    [1],  # 2
    [2],  # 3
    [3,7],    # 4
    [4],    # 5
    [5],  # 6
    [6],    # 7
    [0,10],  # 8
    [7,8],    # 9
    [1,9],    # 10

]
'''D = [
    [10],   # 0  
    [5,2],  # 1
    [3,4],  # 2
    [0,1],  # 3
    [5],    # 4
    [6],    # 5
    [7,4],  # 6
    [4],    # 7
    [7,0],  # 8
    [8],    # 9
    [9],    # 10

]
'''
print(DFS(D))
print(SSK(D))
