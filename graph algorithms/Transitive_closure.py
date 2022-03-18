# złożoność jak Floyda-Warshalla O(V^3)
# spr czy jest mozliwe dojscie z wierzcholka v do u i zapisuje to w macierzy
def Transitive_closure(G):
    n = len(G)
    '''T = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j or G[i][j] > 0:
                T[i][j] = 1
            else:
                T[i][j] = 0'''
    for k in range(n):
        for i in range(n):
            for j in range(n):
                G[i][j] = G[i][j] or (G[i][k] and G[k][j])



G = [
    [1,0,0,0],
    [0,1,1,1],
    [0,1,1,0],
    [1,0,1,1],

]
print(G)
Transitive_closure(G)
print(G)