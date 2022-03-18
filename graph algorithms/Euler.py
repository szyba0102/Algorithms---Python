# Weronika Szybińska
'''graf nieskierowany posiada cykl Eulera wtw.
gdy jest spójny i każdy jego wierzchołek ma parzysty stopień'''

from copy import deepcopy


def euler( G ):
    def DFSVisit(G,u):
        for i in range(n):  # u - wierzchołek z którego wychodzę, i - wierzchołek do którego chce isc
            if G[u][i] == 1:    # jezeli krawedz miedzy wiercholkiem u, a i istnieje przechodze na wiercholek i
                G[u][i] = -1    # kasuje krawędź z macierzy , gdyż już przez nią przeszłam (zamieniam wartość w macierzy na -1)
                G[i][u] = -1
                DFSVisit(G, i)  # szukam dla wierzchołka i, sąsiednich wierchołków do których moge isc i rekurencyjnie wykonuje dla niego te same czynnosci
                Q.append(i)     # po zakonczeniu przetwarzania wierzchołka zapisuje go w liscie

    n = len(G)  # zapisuje w zmiennej n dlugosc boku macierzy (ilosc wierzchołków w grafie)
    Q = []  # tworze liste w której bede zapisywać powstały cykl eulera
    DFSVisit(G,0)   # zaczynam cykl od pierwszego wierzchołka grafu
    Q.append(0)     # po zakonczeniu rekurencji dopisuje wiercholek z którego zaczynałam
    check = True    # sprawdzam warunki konieczne na istnienie cyklu Eulera za pomocom zmiennej check
    for i in range(n):  # sprawdzam warunki oraz naprawiam zmieniona macierz
        c = 0   # zmienna c podliczam ile krawedzi wychodzi z jednego wierzchołka
        for j in range(n):
            if G[i][j] == 1:    # jeżeli w macierzy znajdują sie niezmienione krawędzie , oznacza to ze graf jest niespójny
                check = False
            elif G[i][j] == -1:  # zmieniam wartości -1 na 1
                G[i][j] = 1
                c += 1
        if c % 2 != 0:  # jeżeli ilość krawędzi wychodząca z jednego wierzchołka jest nieparzysta , cykl eulera nie istnieje
            check = False
    if check:   # jeżeli warunki na istnienie cyklu eulera są spełnione zwracam cykl
        return Q

    return None     # jeżeli warunki nie są spełnione zwracam None
  
  
  
  
  
### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik
  
  
G = [[0,1,1,0,0,0],
     [1,0,1,1,0,1],
     [1,1,0,0,1,1],
     [0,1,0,0,0,1],
     [0,0,1,0,0,1],
     [0,1,1,1,1,0]]


GG = deepcopy( G )
cycle = euler( G )

if cycle == None: 
  print("Błąd (1)!")
  exit(0)
  
u = cycle[0]
for v in cycle[1:]:
  if GG[u][v] == False:
    print("Błąd (2)!")
    exit(0)
  GG[u][v] = False
  GG[v][u] = False
  u = v
  
for i in range(len(GG)):
  for j in range(len(GG)):
    if GG[i][j] == True:
      print("Błąd (3)!")
      exit(0)
      
print("OK")