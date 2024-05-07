"""This file contains a simple implementation of a
 graph data structure and example code for creating a graph """

class Graph:
    def __init__(self):
        self._nodes = {}
    def add_node(self,n):
        if n not in self._nodes:
            self._nodes[n] = { }

    def remove_node(self,n):
        if n in self._nodes:
            self._nodes.pop(n)

    def get_nodes(self):
        return self._nodes.keys()


    def add_edge(self, n1, n2, w=0):
        self.add_node(n1)
        self.add_node(n2)
        self._nodes[n1][n2] = w

    def remove_edge(self, n1, n2):
        pass
        if n2 in self._nodes[n1] :
            self._nodes[n1].pop(n2)

    def adjacent(self, n):
        if n in self._nodes:
            return self._nodes[n]

    def len(self):
        return len(self._nodes)


"""-------Entry point-------"""

graph = Graph()
for u,v,w in [ ('a','b',3), ('a','d',2), ('b','c',5), ('c','d',9), ('c','e',1), ('d','e',4)]:
    graph.add_edge(u, v, w)
    print(graph._nodes)
graph.remove_node('a')
print(graph._nodes)



