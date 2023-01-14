import random

class RandomQueue:

    def __init__(self):
        self.queue = []

    # wstawia element w czasie O(1)
    def insert(self, item):
        self.queue.append(item)

    # zwraca losowy element w czasie O(1)
    def remove(self):
        if len(self.queue) >= 1:
            idx = random.randrange(len(self.queue)-1)
            self.queue[idx], self.queue[-1] = self.queue[-1], self.queue[idx]
            return self.queue.pop()

    def is_empty(self):
        return not self.queue

    def is_full(self):
        return False

    # czyszczenie listy
    def clear(self):
        self.queue = []

# Kod testujący moduł.
import unittest

class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue()
        self.queue.insert(4)

    def test_is_empty(self):
        self.assertEqual( self.queue.is_empty(), False )

    def test_remove(self):
        self.queue.insert(1)
        self.queue.insert(2)
        self.queue.insert(3)
        print( self.queue.remove() )

if __name__ == '__main__':
    unittest.main()