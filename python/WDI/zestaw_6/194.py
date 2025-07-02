""""Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. 
Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę napisać 
stosowne deklaracje oraz funkcję redukującą liczbę elementów listy. Na przykład 
lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostać zredukowany
do listy: [13,19] [2,6] [7,12]"""



class Node:
    def __init__(self, data = None):
        self.next = None
        self.beg = data[0]
        self.end = data[1]


def merge(first):
    cur = first
    naste = cur
    while cur.next != None:
        while naste.next != None:
            nast = naste.next
            if cur.beg <= nast.beg <= cur.end or nast.beg <= cur.beg <= nast.end or nast.beg <= cur.end <= nast.end or cur.beg <= nast.end <= cur.end:
                cur.beg = min(cur.beg, nast.beg)
                cur.end = max(cur.end, nast.end)
                naste = naste.next
            naste.naste.next
        cur = cur.next


