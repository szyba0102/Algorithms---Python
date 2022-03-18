#zlozonosc n^2, dziala lepiej niz bubble jak jest posortowana
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



T = [1,4,54,24,5,7,53,42,35,5,45,24,5,4,2,5,567,4,32,234,5543,4]
wstawianie(T)
print(T)