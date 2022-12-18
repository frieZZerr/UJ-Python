"""Klasa reprezentująca węzeł listy jednokierunkowej."""
class Node:

    def __init__( self, data=None, next=None ):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

"""Klasa reprezentująca całą listę jednokierunkową."""
class SingleList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def count(self):
        return self.length

    def insert_head( self, node ):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node

        self.length = self.length+1

    def insert_tail( self, node ):
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = node

        self.length = self.length+1

    def remove_head(self):
        if self.is_empty():
            raise ValueError("The list is empty!")

        node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        node.next = None
        self.length = self.length-1

        return node

    # Zwraca cały węzeł, skraca listę.
    # Dla pustej listy rzuca wyjątek ValueError.
    def remove_tail(self):
        if self.is_empty():
            raise ValueError("The list is empty!")

        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

        self.length -= 1

        return node

    # Węzły z listy other są przepinane do listy self na jej koniec.
    # Po zakończeniu operacji lista other ma być pusta.
    def join( self, other ):
        self.tail.next = other.head
        self.tail = other.tail
        self.length = self.length+other.length

        other.clear()

    def clear(self):
        self.head = self.tail = None
        self.length = 0