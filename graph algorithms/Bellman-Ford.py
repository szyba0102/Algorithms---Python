# złożonosc O(V*E)
# wykorzystywany do szukania najkrotszej sciezki gdy wagi moga byc ujemne
from math import inf

def Bellman_Ford(G,s):
    # inizjalizacja
    n = len(G)
    d = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d[s] = 0

    for i in range(n-1):
        #print(d)
        for x in range(n):
            for y in G[x]:
                if d[y[0]] > d[x] + y[1]:
                    d[y[0]] = d[x] + y[1]
                    parent[y[0]] = x

    for x in range(n):
        for y in G[x]:
            if d[y[0]] > d[x] + y[1]:
                return False
    print(parent)
    return d

G = [
    [[1,4],[2,4]],
    [[2,1],[4,100]],
    [[3,100]],
    [[5,5]],
    [[5,5]],
    [],]


G2=[
    [(1,3),(4,3)],
    [(2,1)],
    [(3,3),(5,1)],
    [(1,3)],
    [(5,2)],
    [(0,6),(3,1)]
]
K = Bellman_Ford(G2,0)
print(K)
# [0, 3, 4, 7, 3, 5]