""""Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy
funkcje:
• inicjalizującą tablicę,
• zwracającą wartość elementu o indeksie n,
• podstawiającą wartość value pod indeks n."""

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class List:
    def __init__(self):
        self.head = Node()
        
    def append(self, data):
        new_node = Node(data)
        cnt = self.head
        while cnt.next != None:
            cnt = cnt.next
        cnt.next = new_node

    def display(self):
        cnt = self.head
        if cnt.data != None:
            print(cnt.data)
        while cnt.next != None:
            print(cnt.next.data)
            cnt = cnt.next

    def length(self):
        cnt = self.head
        count = 0
        while cnt.next != None:
            count += 1
            cnt = cnt.next
        return count

    def element(self, i):
        cnt = self.head
        count = 0
        if i < 0 or self.length() <= i:
            print("Zly indeks")
            return
        while cnt.next != None:
            if count == i:
                print(cnt.next.data)
                return 
            cnt = cnt.next
            count += 1

    def change(self, i, data):
        cnt = self.head
        count = 0
        if i < 0 or self.length() <= i:
            print("Zly indeks")
            return
        while cnt.next != None:
            if count == i:
                cnt.next.data = data
                return 
            cnt = cnt.next
            count += 1

list1 = List()
list2 = List()
list1.append(10)
list1.append(124)
list1.append(5)
list1.display()
list1.element(2)
list1.change(1, 13)
list1.display()




