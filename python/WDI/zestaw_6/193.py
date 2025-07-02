""""Elementy w liście są uporządkowane według wartości klucza. 
Proszę napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. 
Do funkcji przekazujemy wskazanie na pierwszy element listy,
funkcja powinna zwrócić liczbę usuniętych elementów"""

#####################################################################################

class List:
    def __init__(self):
        self.head = Node()
        self.next = None
        
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

    def delete_key(self):
        prev = self.head
        curr = self.head.next
        cnt = 0
        while curr.next != None:
            if curr.next and  curr.data == curr.next.data:
                cnt += 1
                while curr.data == curr.next.data:
                    cnt += 1
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next
    
        print(cnt)

#####################################################################################




class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None



first = List()

first.append(1)
first.append(2)
first.append(2)
first.append(2)
first.append(3)
first.append(4)
first.append(4)
first.append(5)
first.display()

first.delete_key()
