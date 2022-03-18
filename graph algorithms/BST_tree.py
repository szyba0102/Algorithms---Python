#Weronika Szybińska

class BSTNode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def find(root, key):    # funkcja szukająca w drzewie podanej wartości (key)
    while root is not None:
        if root.key == key:
            return root
        elif key<root.key:
            root = root.left
        else:
            root = root. right

    return None

def insert(root,key): # funkcja wstawiająca do drzewa nową wartość
    new = BSTNode(key)
    while root is not None:
        if root.key == key: # jeżeli dana wartośc znajduje sie juz w drzewie to zwracane jest False
            return False
        elif key < root.key: # jeżeli podana wartość key jest mniejsza od wartości w obecnym elemencie to musi sie ona znajdowac po lewej
            if root.left is not None: # jeżeli na lewo znajduje sie element to do niego przechodze
                root = root.left
            else:   # jezeli na lewo elementu nie ma to wstawiam tam nowy element o podaje wartosci key
                root.left = new
                new.parent = root
                return True
        else:   # analogicznie jezeli wartośc jest wieksza to ide na prawo lub jezeli po prawej nie ma elmentu to wsatwiam tam nowy element
            if root.right is not None:
                root = root.right
            else:
                root.right = new
                new.parent = root
                return True


def successor(root):    # funkcja zwracająca wskaźnik na następnika korzenia (root)
    if root.right is not None:
        root = root.right
        while root.left is not None:
            root = root.left
        return root
    else:
        p = root.parent
        while root.parent is not None:
            if p.left is not None and p.left == root:
                return p
            root = p
            p = root.parent
    return False


def remove(root , key): # funkcja usuwająca element z drzewa
    root = find(root,key)   # szukam w drzewie elementu który mam usunąc

    if root is None:    # jezeli takiego elementu w drzewie nie ma zwracam False
        return False

    if root.right is not None and root.left is not None:
    # jezeli element ten (root) ma elemnty przypisane na lewo i prawo, to szukam jego nastepnika, zapisuje wartosc tego nastpnika jako val,
    # usuwam go z drzewa wywolując rekurenycjnie funkcje remove ze wskaznikiem na nastepnik jako argument, a na koniec elementowi root przypisuje wartosc val

        k = successor(root)
        val = k.key
        remove(k,val)
        root.key = val

    elif root.right is not None:
        if root.parent is None:
        # jezeli root nie ma rodzica oznacza ze jest korzeniem drzewa wiec by go usunac podmieniam jego wartosc z wartoscia elemntu po prawej , a nastepnie za pomoc funkcji remove usuwam element root.right
            root.key, root.right.key = root.right.key, root.key
            remove(root.right,root.right.key)
            return True

        p = root.parent # jezeli root ma przypisanego rodzica sprawdzam czy jest on od rodzica na lewo czy na prawo i  usuwam go przepinajac wskazniki
        if p.left == root:
            p.left = root.right
        else:
            p.right = root.right
        root.right.parent = p

    elif root.left is not None: # analogicznie do powyzszego
        if root.parent is None:
            root.key, root.left.key = root.left.key, root.key
            remove(root.left,root.left.key)
            return True

        p = root.parent
        if p.left == root:
            p.left = root.left
        else:
            p.right = root.left
        root.left.parent = p

    else:
    # jezeli root  nie ma elementow na prawo ani lewo, to sprawdzam jakim dzickiem rodzica jest i usuwam go przepinajac wskazniki
        if root.parent is None: # jezeli root nie ma rodzica ani dzieci oznacza to ze jest jedynym elementem w drzewie wiec zmieniam jego wartosc na None
            root.key = None
            return True
        else:
            p = root.parent
        if p.left == root:
            p.left = None
        else:
            p.right = None

    return True














