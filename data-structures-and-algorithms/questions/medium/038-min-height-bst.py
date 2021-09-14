def minHeightBst(array):
    """
    Time: O(n) where n is the number of elements in the array
    Space: O(n)
    """
    return create_min_height_bst(array, 0, len(array) - 1)


def create_min_height_bst(array, start_idx, end_idx):
    if start_idx > end_idx:
        return None

    median_idx = (start_idx + end_idx) // 2

    new_bst = BST(array[median_idx])
    new_bst.left = create_min_height_bst(array, start_idx, median_idx - 1)
    new_bst.right = create_min_height_bst(array, median_idx + 1, end_idx)
    return new_bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
