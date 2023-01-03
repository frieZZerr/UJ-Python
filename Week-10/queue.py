class Queue:

    def __init__(self):
        self.items = []

    # podglądanie kolejki
    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def put(self, data):
        if self.is_full():
            raise ValueError("Queue is full!")

        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")

        return self.items.pop(0)

# Kod testujący moduł.
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.queue.put(4)

    def test_get(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        print( self.queue.get() )
        self.assertEqual( self.queue.is_full(), False )

if __name__ == '__main__':
    unittest.main()