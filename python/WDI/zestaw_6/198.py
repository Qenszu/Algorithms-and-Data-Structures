""""Dana jest lista, który zakończona jest cyklem. 
    Napisać funkcję, która zwraca liczbę elementów przed cyklem"""

from time import sleep

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def is_in_loop(first, note):
    slow = first
    fast = first
    while slow.next != fast:
        slow = slow.next
        fast = fast.next.next
    fast = fast.next
    cur = fast
    while True:
        if cur == note:
            return True
        cur = cur.next
        if cur == fast:
            break
    return False



def num_before_loop(first):
    note = first
    cnt = 0
    while True:
        if is_in_loop(first, note):
            return cnt
        cnt += 1
        note = note.next

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


first = Node(1)
first.next = Node(2)
first.next.next = Node(3)
display(first)
first = append(first, 6)
first = append(first, 7)
first = append(first, 8)
display(first)
first.next.next.next.next.next.next = first
#display(first)
print(num_before_loop(first))
#print(is_in_loop(first, first.next.next.next7))


