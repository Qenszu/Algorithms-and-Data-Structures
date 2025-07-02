""""Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola val i next, której węzły
przechowują liczby naturalne. Liczby przechowywane w liście spełniają warunek ”łączności”, tzn. dla każdego węzła 
ostatnia cyfra liczby jest identyczna z pierwszą cyfrą liczby z następnego węzła. Proszę napisać
funkcję insert(p, n), która wstawia do listy wskazywanej przez wskaźnik p, liczbę n, metodą zastąpienia
co najmniej dwóch elementów jednym zawierającym wstawioną liczbę. Po wstawieniu nowej liczby nadal
zachowany powinien być warunek ”łączności”. Funkcja powinna zwrócić o ile skrócona została lista albo
wartość 0 gdy elementu nie można wstawić do listy.

Na przykład dla listy zawierającej elementy: 2023 31 17 703 37 707 72 29 902
po wstawieniu liczby 303 lista może wyglądać następująco: 2023 303 37 707 72 29 902
Funkcja powinna zwrócić wartość 2."""


class Node:
    def __init__(self, val = None):
        self.next = None
        self.val = val

def append(first, value):
    new_node = Node(value)
    if first is None:
        return new_node
    node = first
    while node.next is not None:
        node = node.next
    node.next = new_node
    
    return first

def display(first):
    node = first
    print(node.val, end = " --> ")
    while node.next != None:
        node = node.next
        print(node.val, end = " --> ")
    print("None")

def first_digit(n):
    while n//10 > 0:
        n = n // 10
    return n


def insert(p, n):
    new_node = Node(n)
    digit1 = first_digit(n)
    wartownik = Node()
    wartownik.next = p                      
    p = wartownik                  # p --> wartownik --> 2023(p.next) --> 31(node1.next.next) --> 17 --> 703 --> 302 --> 2023 --> ...
    node1 = p 
    cnt = 0
    while node1.next.next != p.next:
        node2 = node1.next.next.next.next
        if node1.next.val%10 == digit1:
            node2_first_digit = first_digit(node2.val)
            while node2_first_digit != n%10 and node2.next != node1:
                node2 = node2.next
                node2_first_digit = first_digit(node2.val)
                cnt += 1
                #print(node1.next.val, node2.val ,node2_first_digit)
            if node2.next is not node1:
                node1.next.next = new_node
                new_node.next = node2
                return cnt + 1
        node1 = node1.next
    return 0




first = Node(2023)
first = append(first, 31)
first = append(first, 17)
first = append(first, 703)
first = append(first, 37)
first = append(first, 707)
first = append(first, 72)
first = append(first, 29)
first = append(first, 902)
first.next.next.next.next.next.next.next.next.next = first

#display(first)
print(insert(first, 12))
#first = insert(first, 303)
#display(first)




    