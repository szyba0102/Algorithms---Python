'''Najdluzszy podciąg rosnący
ZLOZONOSC: O(nlogn)'''

def binary_search(A,p,r,k):
    if p > r:
        return r

    mid = p + ((r - p) // 2)
    n = len(A[mid])
    if k == A[mid][n-1]:
        return -1
    elif k > A[mid][n-1]:
        return binary_search(A, mid + 1, r, k)
    else:
        return binary_search(A, p, mid - 1, k)

def LIS(A):
    n = len(A)
    T = [[] for _ in range(n)]
    inx = 0

    T[0].append(A[0])

    for i in range(1,n):
        #print(T)
        if A[i] < T[0][0]:
            T[0][0] = A[i]
        elif T[inx][inx] < A[i] :

            for j in range(len(T[inx])):
                T[inx+1].append(T[inx][j])
            T[inx+1].append(A[i])
            inx += 1
        else:
            r = binary_search(T,0,inx,A[i])
            if r == -1:
                continue
            else:
                for j in range(len(T[r])):
                    T[r + 1][j] = T[r][j]
                T[r+1][r+1] = A[i]
    return T[inx]
#A = [[0,2],[0,1,3],[3,4,4],[5,4,3,6],[3,4,5,8],[9]]
#A = [[3]]
A = [3,4,2,3,7,6,5,6,8,5,9,4]
#print(binary_search(A,0,5,7))
print(LIS(A))