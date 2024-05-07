"""This file contains a simple implementation of a
 tree data structure through a queue and example
 code for creating, manipulating and searching data in a tree"""


import queue_with_deque

class ThreeNode:

    def __init__(self, data=None):
        self._data = data
        self._children = []

    def add_child(self, data=None):
        new_child = ThreeNode(data)
        self._children.append(new_child)
        return new_child

    def remove_child(self, child_node):
        for i in range(len(self._children)):
            if self._children[i] is child_node:
                del(self._children[i])
                break

    def get_children(self):
        return self._children

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def print_dfs_preorder(self):
        print(self.get_data())
        for child in self.get_children():
            child.print_dfs_preorder()

    def print_dfs_postorder(self):
        for child in self.get_children():
            child.print_dfs_postorder()
        print(self.get_data())

    def print_bfs(self):
        nodes = queue_with_deque.Queue()
        node = self
        while node is not None:
            print(node.get_data())
            for child in node.get_children():
                nodes.enqueue(child)
            node = nodes.dequeue()


root_node = ThreeNode(1)
node_2 = root_node.add_child(2)
node_3 = root_node.add_child(3)
node_4 = node_3.add_child(4)
node_3.add_child(5)
node_3.remove_child(node_4)
node_6 = node_2.add_child(6)
node_6 = node_2.add_child(7)

print("Three nodes with Depth-First Search and preorder:")
root_node.print_dfs_preorder()
print("Three nodes with Depth-First Search and postorder:")
root_node.print_dfs_postorder()
print("Three nodes with Breadth-First Search")
root_node.print_bfs()

