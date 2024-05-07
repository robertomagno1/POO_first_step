import queue_with_deque


class BSTNode:

    def __init__(self, data=None, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def add_node(self, data):
            current_node = self
            while True:
                if data <= current_node._data:
                    if current_node._left is None:
                        current_node._left= BSTNode(data)
                        return current_node._left
                    else:
                        current_node = current_node._left
                else:
                    if current_node._right is None:
                        current_node._right= BSTNode(data)
                        return current_node._right
                    else:
                        current_node = current_node._right


    def remove_child(self, child_node):
        if self._left is child_node:
            del self._left
        elif self._right is child_node:
            del self._right

    def get_left_child(self):
        return self._left

    def get_right_child(self):
        return self._right

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def search_node(self, data_to_search):
        if self._data == data_to_search:
            return self
        if data_to_search < self._data:
            if  self._left is None:
                return None
            return self._left.search_node(data_to_search)
        else:
            if  self._right is None:
                return None
            return self._right.search_node(data_to_search)

    def print_dfs_preorder(self):
        print(self._data)
        if self._left:
            self._left.print_dfs_preorder()
        if self._right:
            self._right.print_dfs_preorder()

    def print_dfs_postorder(self):
        if self._left:
            self._left.print_dfs_postorder()
        if self._right:
            self._right.print_dfs_postorder()
        print(self._data)

    def print_dfs_symmetric(self):
        if self._left:
            self._left.print_dfs_symmetric()
        print(self._data)
        if self._right:
            self._right.print_dfs_symmetric()


    def print_bfs(self):
        nodes = queue_with_deque.Queue()
        node = self
        while node is not None:
            print(node.get_data())
            if self._left:
                nodes.enqueue(self._left)
            if self._right:
                nodes.enqueue(self._right)
            node = nodes.dequeue()


root_node = BSTNode(15)
root_node.add_node(2)
root_node.add_node(8)
root_node.add_node(42)
root_node.add_node(54)
root_node.add_node(16)
root_node.add_node(7)

print("Three nodes with Depth-First Search and preorder:")
root_node.print_dfs_preorder()
print("Three nodes with Depth-First Search and postorder:")
root_node.print_dfs_postorder()
print("Three nodes with Depth-First Search and symmetric:")
root_node.print_dfs_symmetric()

value_to_search = 54
print("Searching node with value", value_to_search)

if root_node.search_node(value_to_search) != None:
    print("Node found!")
else:
    print("Node not found!")


