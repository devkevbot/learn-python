# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    """
    Recursive approach.
    Time: O(n^2) where n is the length of the input array
    Space: O(n)

    General strategy:
        For each element in the input array, identify its right child by finding the next
        value in the array which is greater than or equal to the element.

        Recursively find the left and right subtree of each node until all elements are exhausted.

        Recombine each node into a tree.
    """

    if len(preOrderTraversalValues) == 0:
        return None

    curr_value = preOrderTraversalValues[0]
    rst_idx = len(preOrderTraversalValues)

    for idx, value in enumerate(preOrderTraversalValues):
        if value >= curr_value and idx != 0:
            rst_idx = idx
            break

    lst = reconstructBst(preOrderTraversalValues[1:rst_idx])
    rst = reconstructBst(preOrderTraversalValues[rst_idx:])

    return BST(curr_value, lst, rst)


class TreeInfo:
    def __init__(self, root_idx) -> None:
        self.root_idx = root_idx


def reconstructBst(preOrderTraversalValues):
    """
    Alternative approach.
    Time: O(n) where n is the length of the input array
    Space: O(n)
    """

    tree_info = TreeInfo(0)
    return reconstructBstFromRange(
        float("-inf"), float("inf"), preOrderTraversalValues, tree_info
    )


def reconstructBstFromRange(lower, upper, values, subtree_info):
    if subtree_info.root_idx == len(values):
        return None

    root_value = values[subtree_info.root_idx]

    if root_value < lower or root_value >= upper:
        return None

    subtree_info.root_idx += 1

    lst = reconstructBstFromRange(lower, root_value, values, subtree_info)
    rst = reconstructBstFromRange(root_value, upper, values, subtree_info)

    return BST(root_value, lst, rst)
