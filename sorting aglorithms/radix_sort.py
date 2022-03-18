#WYMAGANIA: dane musza dac sie posrtowac leskykograficznie, najlpeiej takiej samej dlugosci lub podobnej
#ZLOZNOSC: d-liczba pozycji, k-zakres wartosci na pozycjach, n-liczba elementow do posrtowania
# typowo O(d(n+k))


def radix_sort(A,d):
    for i in range(1,d):
        pass #use a stable sort to sort array A on digit i :)))

#przyklad z zadania obowizakowego
def countsort(A, k, p):
    C = [0] * k
    B = [0] * len(A)

    for i in range(len(A)):
        C[A[i][p]] += 1

    for i in range(1, k):
        C[i] += C[i-1]

    for i in range(len(A)-1, -1, -1):
        C[A[i][p]] -= 1
        B[C[A[i][p]]] = A[i]

    for i in range(len(A)):
        A[i] = B[i]


def zad_ob_1(A):
    n = len(A)
    for i in range(n):
        b = A[i] % n
        a = A[i] // n
        A[i] = (a,b)

    countsort(A, n, 1)
    countsort(A, n, 0)

    for i in range(len(A)):
        A[i] = A[i][0] * n + A[i][1]

    return A

