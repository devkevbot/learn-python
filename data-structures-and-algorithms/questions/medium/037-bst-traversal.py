def inOrderTraverse(tree, array):
    """
    Time: O(n) where n is the number of nodes in three
    Space: O(n)
    """
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)

    return array


def preOrderTraverse(tree, array):
    """
    Time: O(n) where n is the number of nodes in three
    Space: O(n)
    """
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array


def postOrderTraverse(tree, array):
    """
    Time: O(n) where n is the number of nodes in three
    Space: O(n)
    """
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)

    return array
