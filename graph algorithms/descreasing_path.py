# złożonośc Dijsktry, zapisuej w kolejce piroryetowej kolejno
# (suma dotychczasowej najkrotszej sciezki, wage krawedzi, wierzcholek do ktorego idzemy, jego rodzic)

from queue import PriorityQueue
from math import inf

def dijkstra(G,s,t):

    n=len(G)
    #d = [inf] * n
    K=PriorityQueue()
    path = [t]
    K.put((0,inf,s,-1))
    p = [-1] * n
    T = [[0] * n for _ in range(n)]
    while K:
        u=K.get()
        p[u[2]] = u[3]

        if u[2] == t:
            x = t
            while p[x]!=s:
                path.append(p[x])
                x = p[x]
            path.append(s)
            return u[0],path[::-1]

        for v in G[u[2]]:
            if v[1]<u[1] and T[u[2]][v[0]] == 0:
                K.put((v[1]+u[0],v[1],v[0],u[2]))
                T[u[2]][v[0]] = 1
                T[v[0]][u[2]] = 1

    return False

G=[
    [(2,8),(1,7)],
    [(0,7),(3,6)],
    [(0,8),(3,4),(4,7)],
    [(1,6),(2,4),(4,5),(5,5)],
    [(2,7),(3,5),(5,1)],
    [(3,5),(4,1)]
]

A = [[(1,10),(2,5)],
     [(0,10),(2,1),(3,3),(4,2)],
     [(0,5),(1,1),(3, 6),( 4, 4)],
     [(1, 3),(2, 6),(4, 3),(5, 2)],
     [(1, 2),(2, 4),(3, 3),(5, 1)],
     [(3, 2),(4, 1)],]

B = [
    [(1,9)],
    [(0,9),( 2, 10),(6, 8)],
    [( 1, 10),(3, 4)],
    [(2, 4),(4, 5)],
    [(3, 5),( 5, 6)],
    [(4, 6),(6, 7)],
    [( 2, 8),(5, 7)],
     ]
print(dijkstra(B,0,2))


