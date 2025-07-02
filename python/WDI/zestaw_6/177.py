""""Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. 
    Do funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna 
    zwrócić wskazanie do scalonej listy. Zadanie należy wykonać jako funkcję iteracyjną, a 
    następnie jako funkcję rekurencyjną."""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def mergel(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.data < list2.data:
        list1.next = mergel(list1.next, list2)
        return list1
    else:
        list2.next = mergel(list1, list2.next)
        return list2
    
mergel({2, 5, 6}, {4, 8})
        