# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    """
    Time: O(n) where n is the number of nodes in the tree
    Space: O(d) where d is the max depth of the tree
    """
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, min_bound, max_bound):
    if tree is None:
        return True

    if tree.value < min_bound or tree.value >= max_bound:
        return False

    left_subtree_is_valid = validateBstHelper(tree.left, min_bound, tree.value)
    right_subtree_is_valid = validateBstHelper(tree.right, tree.value, max_bound)

    return left_subtree_is_valid and right_subtree_is_valid
