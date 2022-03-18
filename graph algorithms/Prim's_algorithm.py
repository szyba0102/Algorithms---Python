# złożoność : O(E*logV)
# szuka MST - minimalnego drzewa rozpinajacego
# poprostu leci po najmnijeszych wagach i dodaje do wyniku jezeli krawedz nie idzie do wierzcholka juz przetworzonego
from queue import PriorityQueue
from math import inf

def Prima(G):
    n = len(G)
    Q = PriorityQueue()
    visited = [True for _ in range(n)]
    A = []
    '''for i in range(n):
        Q.put((inf,i))'''

    v = 0 # zaczynam od pierwszego wierzcholka moze byc inny
    visited[v] = False
    for i in G[v]:  # do kolejki dodaje wszyskie krawedzie z niego wychodzace
        Q.put((i[1],v,i[0]))    # krotka - (waga krawedzi, rodzic, dziecko do ktorego ide)
    while not Q.empty():
        u = Q.get()
        x = u[1]
        y = u[2]
        if visited[y]: # spr czy wgl moge rozwac dany wierzchołek
            visited[y] = False # zazanczam ze wierzcholek odwiedzony
            A.append((x,y)) # dodaje do wyniku krawedz
            for i in G[y]:   # dla krawedzi wychodzacyh z naszego wierzcholka
                                # jezeli wierzcholek do ktorego idzie nie byl odwiedzony to dodaj do kolejki
                if visited[i[0]]:
                    Q.put((i[1],u[2],i[0]))
    return A

# przyklad z cormena
A = [
    [(1,4),(2,8)], # 0
    [(0,4),(2,11),(7,8)], # 1
    [(0,8),(3,1),(1,11),(8,7)], # 2
    [(2,1),(8,6),(4,2)], # 3
    [(3,2),(7,4),(5,10),(6,14)], # 4
    [(4,10),(6,9)], # 5
    [(5,9),(4,14),(7,7)], # 6
    [(1,8),(8,2),(4,4),(6,7)], # 7
    [(2,7),(3,6),(7,2)], # 8
]

K = Prima(A)
print(K)