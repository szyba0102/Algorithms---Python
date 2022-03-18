from random import randint, seed


def sort(T, start, finish, middle):
  a = start
  b = middle + 1
  i = 0
  K = [0] * (finish - start + 1)

  while a <= middle and b <= finish:
    if T[a] < T[b]:
      K[i] = T[a]
      i += 1
      a += 1
    else:
      K[i] = T[b]
      i += 1
      b += 1

  if a <= middle:
    while a <= middle:
      K[i] = T[a]
      a += 1
      i += 1
  else:
    while b <= finish:
      K[i] = T[b]
      b += 1
      i += 1

  for x in K:
    T[start] = x
    start += 1

  return T

def rekurencja(T, start, finish):
  lenght = finish - start + 1
  middle = start + (finish - start) // 2

  if lenght >= 2:
    rekurencja(T, start, middle)
    rekurencja(T, middle + 1, finish)

  sort(T, start, finish, middle)

  return T


def mergesort(T):
  l = len(T)
  T = rekurencja(T, 0, (l - 1))
  return T