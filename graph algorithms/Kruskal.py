# O(E*logE)
# grafy nieskierowane , szukanie minimalnego drzewa rozpinajacego (tzn zbior krawedzi laczacyh wszystkie wiercholki)
# idzie po najmniejszych wagach, jak pojscie przez namnijesza wage spowoduje powstanie cyklu,
# to krawedz ta nie jest wybierana (spr czy wierzcholki naleza do jednej rodziny
from queue import PriorityQueue

class Node:
    def __init__(self,val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x):
    if x!=x.parent:
        x.parent = find(x.parent)

    return x.parent

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y: return
    if x.rank>y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank: y.rank+=1

def Kruskal(G):
    n = len(G)
    tree = [Node(i) for i in range(n)]
    A = []
    #s = []
    '''for i in range(n):
        for j in range(1,len(G[i])):
            s.append((i,G[i][j][0],G[i][j][1]))'''
    s = G
    s.sort(key=lambda x: x[2])
    for i in range(len(s)):
        if find(tree[s[i][0]]) != find(tree[s[i][1]]):
            A.append((s[i][0],s[i][1]))
            union(tree[s[i][0]],tree[s[i][1]])
    return A

'''G1 =[
    [0,[1,4],[7,8]],
    [1,[2,1]],
    [2,[3,3],[5,1]],
    [3,[1,3]],
    [4,[5,2]],
    [5,[3,1],[0,6]]
    ]

G2 = [
    [0,4,0,0,0,0,0,8,0],
    [4,0,0,0,0,0,0,11,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [8,11,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    ]'''
G = [(0,1,4),(0,7,8),(1,7,11),(1,2,8),(7,8,7),(2,3,7),(8,6,6),(6,5,2),(2,5,4),(3,5,14),(3,4,9),(5,4,10),(8,2,2),(7,6,1)]
print(Kruskal(G))
