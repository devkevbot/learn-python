"""
Given an array of positive integers, return the maximum sum that can be formed without using adjacent elements.
If the array is empty, return 0.
"""


def maxSubsetSumNoAdjacent(array):
    """
    Time: O(n) where n is the number of elements in the array
    Space: O(1)
    ---
    Hints needed: 3/3
    Time taken: 30 minutes
    """
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    second_last = array[0]
    first_last = max(array[0], array[1])

    for _, val in enumerate(array[2:]):
        if first_last > second_last + val:
            second_last = first_last
        else:
            old_first_last = first_last
            first_last = second_last + val
            second_last = old_first_last

    return first_last
