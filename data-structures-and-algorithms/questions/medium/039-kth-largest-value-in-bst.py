# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    """
    Time: O(h + k) where h is the height of the tree
    Space: O(h + k)
    """
    visited = []
    reverse_in_order_traversal(tree, visited, k)
    return visited[k - 1]


def reverse_in_order_traversal(tree, visited, k):
    if tree is not None and len(visited) < k:
        reverse_in_order_traversal(tree.right, visited, k)
        visited.append(tree.value)
        reverse_in_order_traversal(tree.left, visited, k)
    return
