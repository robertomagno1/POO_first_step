"""This file contains a simple implementation of a
 deque data structure and example code for creating
 and manipulating a deque"""

from collections import deque


class Deque:

    def __init__(self):
        self._data = deque()

    def append(self, e):
        self._data.append(e)

    def appendleft(self, e):
        self._data.appendleft(e)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def popleft(self):
        if self.is_empty():
            return None
        return self._data.popleft()

    def first(self):
        if self.is_empty():
            return None
        return self._data[0]

    def last(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


"""-------Entry point-------"""

my_deque = Deque()
my_deque.append(6)
my_deque.append(2)
l = my_deque.len()
print("Current deque size: ",l)
empty = my_deque.is_empty()
print("Is empty?: ", empty)
my_deque.appendleft(3)
my_deque.append(4)
elem= my_deque.first()
print("Read element : ",elem)
elem = my_deque.pop()
print("Extracted element : ",elem)
elem = my_deque.popleft()
print("Extracted element : ",elem)
elem = my_deque.last()
print("Read element : ",elem)
my_deque.appendleft(9)
l = my_deque.len()
print("Current deque size: ",l)
