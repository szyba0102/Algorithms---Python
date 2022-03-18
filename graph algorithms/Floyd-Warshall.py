# reprezentacja macierzowa
# zlozonosc O(V^3)
# szuka najkrotszych sciezek (z kazdego do kazdego wierzcholka)
# odtworzenie sciezki(druga tablica zapisuja jaki wierzcholek rodziela dane przejscie)
# cofam sie poki rozdzielenei nie skalda sie z tego samego wierzcholka ktory nalezy od danej krawedzi
# 0 w grafie musza byc zamienione na inf oprocz 0 na przekątnej !!!!!!!!!

from math import inf
def Floyd_Warshall(G):
    n = len(G)
    for t in range(n): # na wykladzie (1,n+) inna numeracja wierzchołkow
        for u in range(n):
            for w in range(n):
                G[u][w] = min(G[u][w], G[u][t] + G[t][w])



'''G = [
[inf, 1, 1, inf, 1],
[1, inf, inf, 1, inf],
[1, inf, inf, inf, 1],
[inf, 1, inf, inf, 1],
[1, inf, 1, 1, inf],
]'''
G = [
[0, 1, 6, 7, 7, 3, 7, 3],
[1, 0, 8, 8, 9, 2, 6, 5],
[6, 8, 0, 1, 4, 7, 8, 4],
[7, 8, 1, 0, 5, 7, 8, 5],
[7, 9, 4, 5, 0, 9, 12, 3],
[3, 2, 7, 7, 9, 0, 4, 6],
[7, 6, 8, 8, 12, 4, 0, 9],
[3, 5, 4, 5, 3, 6, 9, 0]
]

Floyd_Warshall(G)
print(G)
n = len(G)
for i in range(n):
    print(G[i])
# K = Floyd_Warshall(G)
# print("......")
# for i in range(n):
#     print(K[i])

