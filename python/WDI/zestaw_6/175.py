""""Proszę zaimplementować zbiór mnogościowy liczb naturalnych korzystając ze struktury
listy odsyłaczowej.
• czy element należy do zbioru
• wstawienie elementu do zbioru
• usunięcie elementu ze zbioru
• sume zbiorow
• czesc wspolna zbiorow"""


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def is_part(first, value):
    while first is not None:
        if first.data == value:
            return True
        first = first.next
    return True

def add(first, value):
    if not is_part(first, value):
        new = Node(value)
        if first:
            next = first.next
            new.next = next
            first.next = new
    else:
        return first

def delete(first, value):
    element = first
    if element.data == value:
        return element.next
    while element is not None:
        if element.next.data == value:
            element.next = element.next.next
        element = element.next
    return first

def suma(list1, list2):
    if list1 is None:
        return list2
    element =  list2
    while list2 is not None:
        if not is_part(list1, element.data):
            n_element = element
            element.next = list1.next
            list1.next = element
            element = n_element
    return list1
