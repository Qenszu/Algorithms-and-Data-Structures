""""Dana jest lista, który zakończona jest cyklem. 
    Napisać funkcję, która zwraca liczbę elementów w cyklu."""



class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def is_loop(first):
    slow = first
    fast = first
    while slow.next != fast:
        slow = slow.next
        fast = fast.next.next
    cur = slow
    cnt = 1
    while cur.next != slow:
        cnt += 1
        cur = cur.next
    return cnt
    

