
def partition(tab, p, r):
  pivot = tab[p]
  i = p - 1
  j = r + 1

  while (True):
    i += 1
    while(tab[i] < pivot):
      i += 1

    j -= 1
    while(tab[j] > pivot):
      j -= 1

    if i >= j:
      return j

    tab[i], tab[j] = tab[j], tab[i]


def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            quick_sort(A, p, q-1)
            p = q + 1
        else:
            quick_sort(A, q+1, r)
            r = q - 1


T = [1,4,54,24,5,7,53,42,35,5,45,24,5,4,2,5,567,4,32,234,5543,4]
quick_sort(T,0,len(T)-1)
print(T)