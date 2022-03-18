# Weronika Szybińska
# złożoność: E*logE
'''Zadanie na podstawie dijkstry , sprawdzam najmniejszą krawędz która dotychczas uzywalismy,
ona nam ograniczy przeplyw reszty'''
from copy import deepcopy
from queue import PriorityQueue
from math import inf

def max_extending_path( G, s, t ):

  n = len(G)  # n - ilość wierzchołków w grafie
  K = PriorityQueue()  # tworzę kolejkę priorytetową (K), do której będę dodawac krotki 3-elementowe:
                       # (-maksymalna przepustowość jaką mamy po dojściu do wierzchołka (wartosci zmieniam na ujemne by kolejka zwracała największe wartości); wierzchołek do którego idziemy; wierzchołek z którego wyszliśmy)
  K.put((-inf, s, -1))  # jako pierwszy element dodaje do kolejki krotke:
                        # (-inf,bo przepustowość jeszcze nie określona; s-wierzchołek do którego idziemy; -1 bo s nie ma rodzica)
  parent = [-1] * n
  visited = [True] * n

  while not K.empty():  # pętla będzie się wykonywać póki nie dojdę do wierzchołka t lub póki kolejka nie będzie pusta
    u = K.get()  # wyciągam z kolejki najmniejszy element (dla nas największy gdyż wartości sa ujemne)
    x = -u[0]  # zmieniam maksymalna przepustowość na dodatnią i zapisuje w zmiennej x
    y = u[1]  # w zmiennej y zapisuje wierzchołek który obecnie będe sprawdzać
    parent[y] = u[2]  # rodzicem y jest wierzchołek z którego przyszliśmy (zapisany w krotce pod indeksem 2)
    if y == t:  # jeżeli obecny wirzchołek to wierzchołek t, to kończe pętle (szłam po maksymalnych przepustowościach więc musi to być dobry wynik)
      path = [t]  # tworze listę w której zapisywać będe szukana scieżkę
      i = t
      while i != s:  # dopóki nie dojde do s dopisuje wierzchołki do ścieżki
        path.append(parent[i])
        i = parent[i]
      path.reverse()
      return path  # zwracam szukaną ścieżke

    visited[y] = False   # zazanczam że obecny wierzchołek został odwiedzony
    for v in G[y]:  # sprawdzam sąsiednie wierzchołki obecnego wierzchołka
      if visited[v[0]]:
        if v[1] <= x:  # jeżeli przepustowość krawędzi miedzy obecnym wierzchołekim a jego sąsiadem ,jest mniejsza od obecnej maksymalnej przepustowości
                       # to dodaje do kolejki nową krotkę ze zmniejszoną maksymalną przepustowością
          K.put((-v[1], v[0], y))
        else:  # w innym wypadku maksymalna przepustowość zostaje taka sama
          K.put((-x, v[0], y))

  return None  # jeżeli funkcja nie znajdzie żadnej ścieżki z s do t, to zwraca None
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1,4), (2,3)], # 0
     [(3,2)], # 1
     [(3,5)], # 2
     []] # 3
s = 0
t = 3
C = 3  


GG = deepcopy( G )
path = max_extending_path( GG, s, t )

print("Sciezka :", path)


if path == []: 
  print("Błąd (1): Spodziewano się ścieżki!")
  exit(0)
  
if path[0] != s or path[-1] != t: 
  print("Błąd (2): Zły początek lub koniec!")
  exit(0)

  
capacity = float("inf")
u = path[0]
  
for v in path[1:]:
  connected = False
  for (x,c) in G[u]:
    if x == v:
      capacity = min(capacity, c)
      connected = True
  if not connected:
    print("Błąd (3): Brak krawędzi ", (u,v))
    exit(0)
  u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
  print("Błąd (4): Niezgodna pojemność")
else:
  print("OK")
  
