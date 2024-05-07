"""This file contains a simple implementation of a
 queue data structure through a list and example
 code for creating and manipulating a queue"""


class Queue:

    def __init__(self):
        self._data = []

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._data.pop(0)

    def first(self):
        if self.is_empty():
            return None
        return self._data[0]

    def len (self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


"""-------Entry point-------"""

my_queue = Queue()
my_queue.enqueue(6)
my_queue.enqueue(2)
l = my_queue.len()
print("Current queue size: ",l)
empty = my_queue.is_empty()
print("Is empty?: ", empty)
elem=my_queue.dequeue()
print("Extracted element : ",elem)
elem=my_queue.dequeue()
print("Extracted element : ",elem)
elem=my_queue.dequeue()
print("Extracted element : ",elem)
my_queue.enqueue(4)
my_queue.enqueue(4)
elem=my_queue.first()
print("Top element : ",elem)
my_queue.enqueue(9)
l = my_queue.len()
print("Current queue size: ",l)