""""Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły
przechowują liczby całkowite. Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie
listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, druga klucze nieparzyste ujemne, pozostałe 
elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki na listę z danymi. Funkcja
powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.
"""

class Node:
    def __init__(self, val = None):
        self.next = None
        self.val = val

def append(p, val):
    node = p
    new_node = Node(val)
    if node.next is None:
        return new_node
    while node.next != None:
        node = node.next
    node.next = new_node
    return p 

def display(p):
    node = p
    print(node.val, " --> ", end = "")
    while node:
        print(node.val, " --> ", end = "")
        node = node.next
    print("None")

first = Node(1)
first = append(first, 4)
display(first)


def seperate(p):
    node1 = Node() #Parzyste dodatnie
    node2 = Node() #Nieparzyste ujemne
    node = p.next
    while node != p:
        if node.val%2 == 0 and node.val >= 0:
            tmp = node
            tmp.next = None
            node1 = append(node1, tmp)


            


