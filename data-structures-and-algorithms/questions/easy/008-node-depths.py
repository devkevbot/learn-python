"""
Return the sum of all nodes' depths.
"""


def calculateNodeDepths(node, parent_depth, list_of_depths):
    if node is None:
        return

    new_depth = parent_depth + 1
    list_of_depths.append(new_depth)

    calculateNodeDepths(node.left, new_depth, list_of_depths)
    calculateNodeDepths(node.right, new_depth, list_of_depths)


def nodeDepths(root):
    """
    My solution
    Time: O(n) - every node is visited
    Space: O(n) - a depth for each node is stored and summed
    """
    list_of_depths = []
    calculateNodeDepths(root, -1, list_of_depths)
    return sum(list_of_depths)


def nodeDepths(root, depth=0):
    """
    Alternative solution #1
    Time: O(n)
    Space: O(h) where h is the height of the tree
    """
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
