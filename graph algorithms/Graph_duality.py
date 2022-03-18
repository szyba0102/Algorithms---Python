

def BFS(G, s):
    Q = []
    n = len(G)
    visited = [False for _ in range(n)]
    #d = [-1 for _ in range(n)]
    #parent = [None for _ in range(n)]
    group = [-1 for _ in range(n)]
    #d[s-1] = 0
    #visited[s-1] = True
    Q.append(s)
    group[s-1] = 0
    while len(Q) !=0 :
        u = Q.pop(0)
        for p in range(1,len(G[u-1])):

            if visited[G[u-1][p]-1] is False:
                visited[G[u-1][p]-1] = True
                #d[G[u-1][p]- 1] = d[u-1] + 1
                #parent[G[u-1][p]-1] = u
                if group[u-1] == 0:
                    group[G[u-1][p]-1] = 1
                else:
                    group[G[u - 1][p] - 1] = 0
                Q.append(G[u-1][p])
            elif group[G[u - 1][p] - 1] == group[u-1]:
                return False



    return True


'''T =  [
        [1,2,3],
        [2,1,5],
        [3,1,4],
        [4,3,5],
        [5,2,4,6],
        [6,5,7],
        [7,6,8],
        [8,7],
]'''
T = [
    [1,3,5,6],
    [2,7],
    [3,1,4],
    [4,3,7],
    [5,1],
    [6,1],
    [7,2,4],
]
K = BFS(T,1)
print(K)

