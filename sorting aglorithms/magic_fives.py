from random import randint, shuffle, seed


def insert_sort(A, p, r):  # typowe sortowanie przez wstawianie używane do posortowania grup 5-elementowych
  i = p + 1
  while i < r:
    val = A[i]
    j = i
    i += 1
    while j > p and A[j - 1] > val:
      A[j] = A[j - 1]
      j = j - 1
    A[j] = val
  return A


def magic_fives(A, p, r):
  # szukam rekurencyjnie mediany median, która będzie piwotem,
  # r jest tutaj liczbą o jeden wieksza od indeksu ostatniego elementu ktory bierzemy pod uwage
  # p jest indeksem pierwszego elementu który bierzemy pod uwage

  if r == p + 1:  # warunek końca rekurencji, gdy znaleziona zostanie ostateczna mediana
    return A

  i = p
  m = (r - p) % 5  # ilosc elementow w ostatniej, niepełnej grupie

  for x in range(p, r - m, 5):  # sortuje kolejne grupy 5-elementowe i przesuwam ich mediany na początek tablicy od indeksu p
    insert_sort(A, x, x + 5)
    A[i], A[x + 2] = A[x + 2], A[i]
    i += 1

  if m != 0:  # sortuje ostatnią niepełna grupe jezeli taka istnieje
    insert_sort(A, r - m, r)
    A[i], A[r - m + (m - 1) // 2] = A[r - m + (m - 1) // 2], A[i]
    i += 1

  return magic_fives(A, p, i)  # wywoluje funkcje dla samych median znajdujących sie na poczatku tablicy


def partition(A, p, r):

  magic_fives(A, p, r + 1)  # zwracam tablice w ktorej pod indeksem p lezy mediana median elementow od indeksu p do r

  A[p], A[r] = A[r], A[p]  # zamieniam miejsce mediany czyli naszego piwota by lezał pod indeksem r
  x = A[r]  # wyznaczam wartosc piwota
  i = p - 1
  for j in range(p, r):  # sortuje tablice ze względu na piwot
    if A[j] <= x:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i + 1], A[r] = A[r], A[i + 1]

  return i + 1


def select(A, p, r, k):  # glowna funkcja wykonujaca sortowanie tablicy w zaleznosci od polozenia k wzgledem piwota
  if p == r:
    return A[p]

  q = partition(A, p, r)

  if q == k:
    return A[q]
  elif k < q:
    return select(A, p, q - 1, k)
  else:
    return select(A, q + 1, r, k)

def linearselect( A, k ): #wywolanie glownej funkcji

  return select(A, 0, len(A) - 1, k)





