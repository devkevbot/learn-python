"""Traverse the tree in depth-first fashion and record all names of the nodes as you do so."""

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        """
        My solution
        Time: O(v + e) where v is the number of nodes and e is the number of edges
        Space: O(v) where v is the number of nodes
        """

        array.append(self.name)

        for child in self.children:
            child.depthFirstSearch(array)

        return array
