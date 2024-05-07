"""This file contains a simple implementation of a
 queue data structure through a deque and example
 code for creating and manipulating a queue"""

from collections import deque

class Queue:

    def __init__(self):
        self._data = deque()

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._data.popleft()

    def first(self):
        if self.is_empty():
            return None
        return self._data[0]

    def len (self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


def main():
    my_stack = Queue()
    my_stack.enqueue(6)
    my_stack.enqueue(2)
    l = my_stack.len()
    print("Current stack size: ",l)
    empty = my_stack.is_empty()
    print("Is empty?: ", empty)
    elem=my_stack.dequeue()
    print("Extracted element : ",elem)
    elem=my_stack.dequeue()
    print("Extracted element : ",elem)
    elem=my_stack.dequeue()
    print("Extracted element : ",elem)
    my_stack.enqueue(4)
    my_stack.enqueue(4)
    elem=my_stack.first()
    print("Top element : ",elem)
    my_stack.enqueue(9)
    l = my_stack.len()
    print("Current stack size: ",l)


"""-------Entry point-------"""

if __name__ == "__main__":
    main()