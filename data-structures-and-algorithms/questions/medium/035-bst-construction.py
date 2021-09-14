# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
from typing import Counter


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Time: O(logn) average, O(n) worst
        Space: O(logn) average, O(n) worst
        """
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        """
        Time: O(logn) average, O(n) worst
        Space: O(logn) average, O(n) worst
        """
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    def remove(self, value, parent=None):
        """
        Time: O(logn) average, O(n) worst
        Space: O(logn) average, O(n) worst
        """
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            # If the node has two children, swap the node's
            # value with the min value from the right child's subtree,
            # then delete the min value
            if self.left is not None and self.right is not None:
                self.value = self.right.find_min()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right

        # Do not edit the return statement of this method.
        return self

    def find_min(self):
        if self.left is None:
            return self.value
        else:
            return self.left.find_min()


# Iterative solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Time: O(logn) average, O(n) worst
        Space: O(1) average, O(1) worst
        """

        current_node = self

        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            elif value >= current_node.value:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        """
        Time: O(logn) average, O(n) worst
        Space: O(1) average, O(1) worst
        """

        current_node = self

        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.right:
                current_node = current_node.right
            else:
                # We found the value
                return True

        return False

    def remove(self, value, parent=None):
        """
        Time: O(logn) average, O(n) worst
        Space: O(1) average, O(1) worst
        """

        current_node = self

        while current_node is not None:
            if value < current_node.value:
                parent = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent = current_node
                current_node = current_node.right
            else:
                # Node with two children
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.find_min()
                    # remove smallest node of right subtree
                    current_node.right.remove(current_node.value, current_node)
                # root node has no parent node
                if parent is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # no children
                        current_node.value = None
                # left child
                elif parent.left == current_node:
                    parent.left = (
                        current_node.left
                        if current_node.left is not None
                        else current_node.right
                    )
                # right child
                elif parent.right == current_node:
                    parent.right = (
                        current_node.left
                        if current_node.left is not None
                        else current_node.right
                    )
                break

        # Do not edit the return statement of this method.
        return self

    def find_min(self):
        current_node = self

        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value
