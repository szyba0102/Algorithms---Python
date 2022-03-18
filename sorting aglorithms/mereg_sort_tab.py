from random import randint
from time import time


class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def getdata(n):
    return [randint(0, 20) for _ in range(n)]


def upload(fir, T):
    T.reverse()
    for elem in T:
        p = Node(elem)
        p.next = fir
        fir = p
    return fir


def read(fir):
    while fir is not None:
        print(fir.val, end=' ')
        fir = fir.next
    print()


def get_two(first):
    if first.next is None:
        return first

    temp = first
    temp2 = first
    count = 1
    while first is not None:
        first = first.next
        count += 1
    for _ in range(count // 2 - 1):
        temp2 = temp2.next

    first = temp2
    temp2 = temp2.next
    first.next = None
    return temp, temp2


def merge_sort(first):
    if first.next is None:
        return first

    else:
        left, right = get_two(first)
        left = merge_sort(left)
        right = merge_sort(right)
        first = merge(left, right)

    return first


def merge(fir1, fir2):
    new_first = Node(None)
    new = new_first

    while fir1 is not None and fir2 is not None:
        if fir1.val > fir2.val:
            new.next = fir2
            fir2 = fir2.next
            new = new.next
            new.next = None
        else:
            new.next = fir1
            fir1 = fir1.next
            new = new.next
            new.next = None

    if fir1 is None:
        new.next = fir2

    elif fir2 is None:
        new.next = fir1

    return new_first.next



if __name__ == '__main__':
    first = None
    first = upload(first, getdata(5))
    read(first)
    first = merge_sort(first)
    read(first)