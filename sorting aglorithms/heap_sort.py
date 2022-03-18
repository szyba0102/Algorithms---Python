'''HEAP
Kopiec - drzewo binarne, gdzie każdy węzeł ma wartość >= niż jego dzieci
Reprezentowane przez tablice.
left(i) = 2i+1
right(i) = 2i+2
parent(i) = podłoga z ((i-1)/2) czyli tak naprawde (i-1)//2
O(logn) - czas działania heapify
O(nlogn) - czas działania buildheap
O(nlogn) - czas działania heapsorta
'''
def left(i):    # lewe dziecko
    return 2*i+1

def right(i):   # prawe dziecko
    return 2*i+2

def parent(i):  # rodzic
    return (i-1)//2

def heapify(A, n, i):   # czas działania O(logn), działa dla JEDNEGO zepsutego elementu i w kopcu
    # naprawianie kopca, n-dlugosc częsci tablicy którą naprawiamy, i - obecny indeks
    l = left(i) # lewe dziecko
    r = right(i)    # prawe dziecko
    m = i   # obecny indeks
    if l < n and A[l] > A[m]: m = l # jeżeli dziecko istnieje oraz jest wartość jest wieksza od obecnego elementu:
                                    # to m staje sie dzieckiem

    if r < n and A[r] > A[m]: m = r # analogicznie
    # ostatecznie pod m jest indeks do wartosci największej z tych trzech

    if m != i:  # jeżeli  nam sie zmieniło
        A[i], A[m] = A[m], A[i]    # zamieniamy wartości
        heapify(A,n,m) # idziemy w dół i sprawdzamy czy wszystko jest okej

def build_heap(A):   # budowanie kopca z tablicy A, działanie O(nlogn)
    n = len(A)
    for i in range(parent(n-1), -1, -1):
    # ide od rodzica na końcu tablicy idąc do tyłu aż do 0
        heapify(A,n,i)

def heapsort(A):    # O(nlogn)
    # ide od rodzica ostateniego elementu do indeksu 1  i sprawdzam czy dane element jest on ustwiony poprawnie
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1):
        A[0], A[i] = A[i], A[0]
        heapify(A,i,0)

def heap_insert(A,x):
    inx = len(A)
    A = A + [x]
    parent = (inx-1)//2
    while A[inx] > A[parent]:
        A[inx], A[parent] = A[parent], A[inx]
        inx = parent
        parent = (inx-1)//2
    return A


if __name__ == '__main__':
    A = [10,17,11,7,1,12]
    print(A)
    build_heap(A)
    print(A)
    #heapsort(A)
    #A = heap_insert(A,10)
    print(A)