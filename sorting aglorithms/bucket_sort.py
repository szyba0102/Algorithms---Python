# WYMAGANIA: liczby z zakresu [0, 1] ([0, k] z normalizacją)
# musimy znać liczbę kubełków n (przynajmniej w przybliżeniu)
#najlepiej rozkład jednostajny

#ZLOZNOSC: O(n) - rozkład jednostajny, O(n2) - tablica z liczbami jednej wartości
# im bardziej jednostajny rozkład, tym bardziej liniowe
# typowo O(d(n+k))

#IDEA: robimy listę n “kubełków”, czyli zakresów długości 1/n, każdy reprezentujemy jako listę, a następnie
# “wrzucamy” nasze liczby do odpowiednich “kubełków”, sortujemy je i przepisujemy do tablicy wynikowej

#NORMALIZACJA: na potrzeby liczenia, do którego kubełka powinien trafić element dzielimy go przez
#największy element z tablicy - wtedy wszystkie będą w zakresie [0, 1]; wrzucamy do niego jednak niezmieniony element!

def bucket_sort(T):
    n = len(T)
    B = []
    for i in range(0,n-1):
        #make B[i] an empty list (?)
        #stworz wartownikow dal kazdego indeksu
        pass
    for i in range(1,n):
        #insert A[i] into list B[nA[i]]
        #dolaczaj do danego wskaznika (pudelka) kolejne wartosci
        pass
    for i in range(0,n-1):
        #sort list B[i] with insertion sort
        #posrtuj listy, (a nie lepiej odrazu dolacza w dobre miejsce?)
        pass
    #concatenate the list B[0],B[1],...,B[n-1] together in order
    #polacz wszystkie listy , PAMIETAJ O USUNIECIU WARTOWNIKOW!!!!!

    def bucket_sort2(arr, n):
        norm = max(arr) #maksymalny element
        buckets = [[] for _ in range(n)]  # list of n empty lists

        for num in arr:
            norm_num = num / norm  # normalized num
            buck_ind = int(n * norm_num)  # select bucket
            buckets[buck_ind].append(num)  # add num to bucket

        for i in range(n):
            buckets[i] = sorted(buckets[i])

        output = []
        for i in range(n):  # i-th bucket
            for j in range(len(bucket[i])):  # j-th element
                output.append(bucket[i][j])

        return output
