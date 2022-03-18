# computational complexity: n^2

def bubble_sort(T):
    n = len(T)
    for i in range(n - 1):
        for j in range(n - 1):
            if T[j] > T[j + 1]:
               T[j], T[j + 1] =T [j + 1], T[j]


