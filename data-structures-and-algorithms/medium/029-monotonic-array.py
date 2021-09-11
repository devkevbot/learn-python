"""
Return true if the array is either monotonically increasing or monotonically decreasing.
"""


def isMonotonic(array):
    """
    Time: O(n) - we iterate through the array once
    Space: O(1) - we don't allocate any input-dependent memory
    """
    isNonDecreasing = True
    isNonIncreasing = True

    for index in range(1, len(array)):
        if array[index] > array[index - 1]:
            isNonIncreasing = False
        if array[index] < array[index - 1]:
            isNonDecreasing = False

    return isNonDecreasing or isNonIncreasing
