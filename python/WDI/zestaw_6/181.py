""""Proszę napisać funkcję usuwającą ostatni element listy. 
    Do funkcji należy przekazać wskazanie na pierwszy element listy."""

class Node: 
    def __init__(self, data):
        self.next = None
        self.data = data

def delete(first):
    ind = first
    if first.next is None:
        return None
    while ind.next.next is not None:
        ind = ind.next
    ind.next = None
