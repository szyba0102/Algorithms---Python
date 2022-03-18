# zlozonosc:
# reprezentacja listowa : O(V+E)
# reprezentacja maceirzowa O(V^2)


from collections import deque

def BFS(G, s,v):
    Q = deque()
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]

    d[s] = 0
    visited[s] = True
    Q.append(s)
    while Q :
        u = Q.popleft()
        # otrzymywanie drogi
        '''if u == v:
            result = [v]
            head = parent[u]
            while head != -1:
                result.append(head)
                head = parent[head]
            return result'''
        for p in G[u]:
            if visited[p] is False:
                visited[p] = True
                d[p] = d[u] + 1
                parent[p] = u
                Q.append(p)
                #print(G[u-1][p])
                #print(Q)

    return visited, d, parent


'''K = [
    [1,2],
    [0,3,4],
    [0,4],
    [1,5],
    [1,2,5],
    [3,4],
]'''
K = [[1, 2], [0, 3], [0, 3], [1, 2]]
#print(BFS(K,0,3))
m,l,n = BFS(K,0,3)
print(m)
print(l)
print(n)