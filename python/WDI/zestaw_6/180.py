"""Proszę napisać funkcję wstawiającą na koniec listy nowy element. 
    Do funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą wartość."""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

def append(first, value):
    node = first
    new_node = Node(value)
    if first is None:
        return new_node
    while node.next != None:
        node = node.next
    node.next = new_node

    return first


first = Node(1)
first.next = Node(2)
first = append(first, 3)
first = append(first, 4)

node = first
while node.next != None:
    print(node.value)
    node = node.next
print(node.value)
    