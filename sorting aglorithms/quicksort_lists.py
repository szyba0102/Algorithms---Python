class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def partition(first):
    pivot = first.val
    temp = first
    first = first.next
    fir_l = Node(None)
    fir_e = Node(None)
    fir_r = Node(None)
    left, right, middle = fir_l, fir_r, fir_e

    while first is not None:

        if first.val > pivot:
            right.next = first
            first = first.next
            right = right.next
            right.next = None

        elif first.val < pivot:
            left.next = first
            first = first.next
            left = left.next
            left.next = None

        else:
            middle.next = first
            first = first.next
            middle = middle.next
            middle.next = None

    middle.next = temp
    middle = middle.next
    middle.next = None
    return fir_l.next, fir_e.next, fir_r.next, middle


def get_last(first):
    if first is None:
        return None
    while first.next is not None:
        first = first.next
    return first


def connect(left, right, middle, mend):
    new_list = Node(None)
    first = new_list
    if left is not None:
        new_list.next = left
        new_list = get_last(left)
    if middle is not None:
        new_list.next = middle
        new_list = mend
    if right is not None:
        new_list.next = right

    return first.next


def quicker_sort(first):
    if first is None:
        return first
    else:
        left, mid, right, mend = partition(first)
        left = quicker_sort(left)
        right = quicker_sort(right)
        first = connect(left, right, mid, mend)

    return first

def create(first,element):
    p = first
    r = None
    while p is not None:
        r = p
        p = p.next

    q = Node(element)
    if r is None:
        q.next = p
        return q

    r.next = q
    q.next = p
    return first

def wypisz(p):
    while p is not None:
        print(p.val, end = " ")
        p = p.next

T = [3,2,45,3,2,2,3,5,2,1]
first = None
second = None
T2 = [70,34,5,3,23]
for x in T:
    first = create(first,x)
wypisz(first)
first = quicker_sort(first)
print("l")
#wypisz(first)
#first = conect(first,second)
#first, second = partition(first)
wypisz(first)
print()
#wypisz(second)