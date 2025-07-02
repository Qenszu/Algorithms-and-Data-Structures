""""Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność 
    jej elementów."""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def revers(first):
    el1 = first
    el2 = None
    
    while el1 is not None:
        next_node = el1.next
        el1.next = el2
        el2, el1 = el1, next_node
    return el2
   