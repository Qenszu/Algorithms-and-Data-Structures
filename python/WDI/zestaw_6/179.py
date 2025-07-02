""""Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według
ostatniej cyfry pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która
jest posortowana niemalejąco według ostatniej cyfry pola val."""

class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class List:
    def __init__(self):
        self.head = Node()

    def append(self, val):
        node = self.head
        new_node = Node(val)
        while node.next != None:
            node = node.next
        node.next = new_node

    def display(self):
        node = self.head
        if node.data != None:
            print(node.data)
        while node.next != None:
            print(node.next.data)
            node = node.next
        

list1 = List()
list1.append(10)
list1.display()

def seperate(first):
    node = first
    
