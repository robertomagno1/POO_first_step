"""This file contains a simple implementation of a
 stack data structure and example code for creating
 and manipulating a stack"""

class Stack:

    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def top(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0


"""-------Entry point-------"""

my_stack = Stack()
my_stack.push(6)
my_stack.push(2)
l = my_stack.len()
print("Current stack size:",l)
empty = my_stack.is_empty()
print("Is empty?:", empty)
elem=my_stack.pop()
print("Extracted element:",elem)
elem=my_stack.pop()
print("Extracted element:",elem)
elem=my_stack.pop()
print("Extracted element:",elem)
my_stack.push(4)
my_stack.push(4)
elem=my_stack.top()
print("Top element:",elem)
my_stack.push(9)
l = my_stack.len()
print("Current stack size:",l)



