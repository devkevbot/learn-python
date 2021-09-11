"""
Return true if the array is either monotonically increasing or monotonically decreasing.
"""


def isMonotonic(array):
    """
    Time: O(n) - we iterate through the array once
    Space: O(1) - we don't allocate any input-dependent memory
    """
    is_non_decreasing = True
    is_non_increasing = True

    for index in range(1, len(array)):
        if array[index] > array[index - 1]:
            is_non_increasing = False
        if array[index] < array[index - 1]:
            is_non_decreasing = False

    return is_non_decreasing or is_non_increasing
