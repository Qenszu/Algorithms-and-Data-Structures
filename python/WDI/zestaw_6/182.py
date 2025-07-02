""""Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji
należy przekazać wskazanie na pierwszy element listy"""


class Node:
    def __init__(self, val = None):
        self.next = None
        self.val = val

def length(first):
    node = first
    if node.next == None:
        return 0
    cnt = 1
    while node.next != None:
        cnt += 1 
        node = node.next
    return cnt


def delete(first):
    node = first
    if length(node) == 0:
        return first
    elif length(node) == 1:
        node.next = None
        return first
    else: 
        if length(node)%2 != 0:
            while node.next.next != None:
                node.next = node.next.next
                node = node.next
                if node.next == None:
                    return first
        else:
            while node.next.next != None:
                node.next = node.next.next
                node = node.next
            node.next = None
    

    return first

first = Node(1)
first.next = Node(2)
first.next.next = Node(3)
first.next.next.next = Node(4)
first.next.next.next.next = Node(5)

first = delete(first)


node = first
while node.next != None:
    print(node.val)
    node = node.next
print(node.val)
    