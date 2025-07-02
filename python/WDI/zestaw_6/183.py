""""Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy
listy przechowują kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1."""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def append(first, value):
    node = first
    new_node = Node(value)
    if node.next == None:
        return new_node
    while node.next != None:
        node = node.next
    node.next = new_node
    return first

def display(first):
    node = first
    print(node.data, end = " --> ")
    while node.next != None:
        node = node.next
        print(node.data, end = " --> ")
    print("None")



first = Node(9)
first.next = Node(9)
first.next.next = Node(9)
first = append(first, 9)
first = append(first, 9)
first = append(first, 9)



def revers(first):
    node = first
    next_node = None
    while node != None:
        tmp = node.next
        node.next = next_node
        next_node, node = node, tmp
    return next_node




def przenies(first):
    node = first
    node_1 = Node(1)
    while node.next != None:
        while node.data == 10 and node.next != None:
            node.data = 0
            node.next.data = node.next.data + 1
        node = node.next
    if node.data == 10:
        node.data = 0
        node.next = node_1


    return first


def plus_one(first):
    node = first
    while node.next != None:
        node = node.next
    node.data += 1
    first = przenies(revers(first))
    
    return revers(first)

display(first)
first = plus_one(first)
display(first)

    

 