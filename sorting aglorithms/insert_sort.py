# computational complexity: n^2
# zlozonosc n^2, dziala lepiej niz bubble jak jest posortowana
def wstawianie(T):
    i = 1
    while (i < len(T)):
        val = T[i]
        j = i
        i += 1

        while (j > 0 and T[j - 1] > val):
            T[j] = T[j - 1]
            j = j - 1

        T[j] = val


