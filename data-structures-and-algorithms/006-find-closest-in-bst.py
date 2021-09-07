def findClosestHelper(tree, target, closest):
    """
    Recursive implementation
    Average: O(logn) time and O(logn) space
    Worst: O(n) time and O(n) space
    """
    if tree is None:
        return closest

    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestHelper(tree.left, target, closest)

    if target > tree.value:
        return findClosestHelper(tree.right, target, closest)

    return closest


def findClosestHelper(tree, target, closest):
    """
    Iterative implementation
    Average: O(logn) time and O(1) space
    Worst: O(n) time and O(1) space
    """

    current = tree
    while current is not None:
        if abs(target - closest) > abs(target - current.value):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            break

    return closest


def findClosestValueInBst(tree, target):
    return findClosestHelper(tree, target, tree.value)

# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
