""""Dana jest liczba odsyłaczowa, której elementy przechowują niepuste napisy składające się z małych
liter alfabetu angielskiego. Proszę napisać funkcję make_order(p), która porządkuje elementy listy tak,
aby na jej początku znalazły się napisy, w których kolejne litery są w porządku rosnącym, natomiast
na końcu listy znalazły się napisy, w których litery są w porządku malejącym. Pomiędzy powstałymi
grupami elementów należy wstawić elementy zawierające pusty napis. Do funkcji należy przekazać
wskaźnik do pierwszego elementu listy, funkcja powinna zwrócić wskazanie do uporządkowanej listy.


Na przykład lista: ala → ola → abel → ula → irys → ewa → sroka → gips
Po uporządkowaniu może mieć postać: abel → gips → „” → irys → ala → ewa → „” → sroka → ola → ula"""

class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

def alf(n):
    alfabetycznie = True
    analfabetycznie = True
    for i in range(len(n)-1):
        if n[i]<n[i+1]: analfabetycznie = False
        if n[i]>n[i+1]: alfabetycznie = False

    if analfabetycznie:
        return 2
    if alfabetycznie:
        return 0
    return 1

def display(first):
    node = first
    print(node.val, end = " --> ")
    while node.next != None:
        node = node.next
        print(node.val, end = " --> ")
    print("None")

first = Node("ala")
first.next = Node("ola")
first.next.next = Node("abel")
first.next.next.next = Node("ula")
first.next.next.next.next = Node("irys")
first.next.next.next.next.next = Node("ewa")
first.next.next.next.next.next.next = Node("sroka")
first.next.next.next.next.next.next.next = Node("gips")


def make_order(p):
    node1 = Node()
    node1.next = Node("'',,")
    node2 = node1.next
    node2.next = Node("'',,")
    node3 = node2.next             # node1('',,) --> node2('',,) --> node3(None)
    while p != None:
        order = alf(p.val)
        if order == 0:
            q = node1
        elif order == 1:
            q = node2
        elif order == 2:
            q = node3
        tmp = q.next                          #q = node1  tmp --> node2 --> node3
        q.next = p                            #q --> ala --> ola --> abel
        p.next, p = tmp, p.next               
    display(node1.next)

make_order(first)
            
    



