# złożoność: O(E*logV) dla listy, O(V^2) dla macierzy
# szuka najkrótdzych ścieżek gdy wagi sa nieujemne
# idzie po kolejnych wierzchołkach, w kolejce

from queue import PriorityQueue
from math import inf

def dijkstra(G,v):

    n = len(G)
    d = [inf for _ in range(n)]
    d[v] = 0
    K=PriorityQueue()

    K.put((d[v], v))
    visited = [False for _ in range(n)]
    p = [-1 for _ in range(n)]

    while not K.empty():
        u=K.get()
        x = u[0]    # obecna odległość
        y = u[1]    # wierzchołek obecny
        if visited[y] is False:
            visited[y] = True
            for v in G[y]:
                if d[v[0]] > d[y] + v[1]:
                    d[v[0]]=d[y]+v[1]
                    p[v[0]]=y
                    K.put((d[v[0]],v[0]))

    return d

G=[
    [(1,3),(4,3)],
    [(2,1)],
    [(3,3),(5,1)],
    [(1,3)],
    [(5,2)],
    [(0,6),(3,1)]
]
'''G = [
    [[1,4],[2,4]],
    [[2,1],[4,100]],
    [[3,100]],
    [[5,5]],
    [[5,5]],
    [],
]'''
print(dijkstra(G,0))
#[0, 3, 4, 6, 3, 5]