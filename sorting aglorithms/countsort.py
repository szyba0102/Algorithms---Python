
# WYMAGANIE: zakres wartiść w tablicy ograniczony do liczb naturaknych [0,k]
# ZLOZONOSC O(k+n), dla k=O(n) daje to O(n) -> k musi byc proporcjonalne do tablicy
# STABILNY

def countsort(T,k,x):
    C = [0] * k
    B = [0] * len(T)
    for i in range(len(T)):
        C[T[i][x]] += 1  #dodajemy do indeksu imitujacego liczbe +1 jak owa liczba wystepuje
    for i in range(1,k):
        C[i] += C[i-1] #do kolejnych ideksow dodajemy wartsco poprzedniego
    for i in range(len(T)-1,-1,-1):
        C[T[i]] -= 1            #idzie od ostatniego ideksu tablicy T,sprawdza co stoi pod tym ideksem a nastpenie co stoi
        B[C[T[i]]] = T[i]       #pod indeksem rownym owej liczbie w tablicy C, nastpnie odjemuje od liczby pod tym ideksem
                                #w tablicy C -1 dzieki czemu powsatje powiedzmy zmienna x
                                # zmienna x jest nowym indkesem dla tablicy C, pod tym ideksem zapisujemy liczbe z tablicy
                                #T z pod indeksu początkowego i
    for i in range(len(T)):
        T[i] = B[i] #przepisujemy posortowane warosci do tablicy  poczatkowej

    return T

T = [3,2,4,5,3,2,3,5,6,4,3,2]
countsort(T,10)
print(T)