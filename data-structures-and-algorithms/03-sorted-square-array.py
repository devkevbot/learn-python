"""
Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length
with the squares of the original integers also sorted in ascending order.
"""


def sortedSquaredArray(array):
    """
    Naive approach

    O(nlogn) time and O(n) space
    Time: Sorting is O(nlogn) at best!
    Space: New array of n elements is O(n) space
    """

    squared_array = [x*x for x in array]
    squared_array.sort()
    return squared_array


def sortedSquaredArray(array):
    """
    Right-to-left pointer approach

    O(n) time and O(n) space
    Time: Because the array is sorted, we can solve in linear time
    Space: New array of n elements is O(n) space
    """

    small_index = 0
    large_index = len(array) - 1
    sorted_values = [0 for _ in array]

    # Right to left
    for index in reversed(range(len(array))):
        small = array[small_index]
        large = array[large_index]

        if abs(small) > abs(large):
            sorted_values[index] = small * small
            small_index += 1
        else:
            sorted_values[index] = large * large
            large_index -= 1
    return sorted_values
