'''WYMAGANIA: liczby z zakresu [0, 1] ([0, k] z normalizacją)
musimy znać liczbę kubełków n (przynajmniej w przybliżeniu)
najlepiej rozkład jednostajny

ZLOZNOSC: O(n) - rozkład jednostajny, O(n2) - tablica z liczbami jednej wartości
im bardziej jednostajny rozkład, tym bardziej liniowe typowo O(d(n+k))

IDEA: robimy listę n “kubełków”, czyli zakresów długości 1/n, każdy reprezentujemy jako listę, a następnie
“wrzucamy” nasze liczby do odpowiednich “kubełków”, sortujemy je i przepisujemy do tablicy wynikowej

NORMALIZACJA: na potrzeby liczenia, do którego kubełka powinien trafić element dzielimy go przez
największy element z tablicy - wtedy wszystkie będą w zakresie [0, 1]; wrzucamy do niego jednak niezmieniony element!'''

class Node:
    def __init__(self):
        self.next = None
        self.Value = None

def tab2list( A ): # tworzy liste
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.value = A[i]
        C.next = X
        C = X
    return H.next

def printlist( L ):
    while L != None:
        print( L.value, "->", end=" ")
        L = L.next
    print("|")


def sort_wstawianie(T): # sortowanie przez wtsawianie (n^2) lecz na małej ilosci elementów bardziej optymalne
    i = 1
    while (i < len(T)):
        val = T[i]
        j = i
        i += 1
        while (j > 0 and T[j - 1] > val):
            T[j] = T[j - 1]
            j = j - 1
        T[j] = val

def which_bucket(x,n):
    for i in range(n):
        if x < (i+1)/n and x > i/n:
            return i

def bucketsort(A):
    n = len(A)
    buckets = [[] for _ in range(n)]
    for i in range(n):
        inx = which_bucket(A[i],n)  # sprawdza który kubełek
        buckets[inx].append(A[i])   # dodaje element do odpowiedniego kubełka
    for i in range(n):
        sort_wstawianie(buckets[i]) # sortuje kolejne kubełki
    i = 0
    for j in range(n):  # przepisywanie do wyjesciowej tablicy
        for k in buckets[j]:
            A[i] = k
            i += 1



A = [0.42,0.13,0.07,0.21,0.91,0.13,0.37]
bucketsort(A)
print(A)
