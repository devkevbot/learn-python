"""
Given a sorted array, return the index of a target number if it exists, or -1 if it does not.
"""


def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    """
    Recursive solution
    Time: O(log(n)), where n is the length of the input array
    Space: O(log(n))
    """
    if left > right:
        return -1

    middle_index = calculateMiddleIndex(left, right)
    middle_value = array[middle_index]

    if target == middle_value:
        return middle_index
    elif target > middle_value:
        return binarySearchHelper(array, target, middle_index + 1, right)
    else:
        return binarySearchHelper(array, target, left, middle_index - 1)


def calculateMiddleIndex(left, right):
    return (left + right) // 2


def binarySearchHelper(array, target, left, right):
    """
    Iterative solution
    Time: O(log(n)), where n is the length of the input array
    Space: O(1)
    """

    while left <= right:
        middle_index = calculateMiddleIndex(left, right)
        middle_value = array[middle_index]

        if target == middle_value:
            return middle_index
        elif target > middle_value:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return -1
