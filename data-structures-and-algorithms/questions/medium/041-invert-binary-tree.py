def invertBinaryTree(tree):
    """
    Time: O(n) where n is the number of nodes in the tree
    Space: O(d) where d is the max depth of the tree
    """
    if tree is None:
        return

    swapChildren(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapChildren(tree):
    tree.left, tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
