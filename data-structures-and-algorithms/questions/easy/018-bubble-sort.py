"""
Return an array that is sorted in ascending order.
Implement bubble sort to sort the array.
"""


def bubbleSort(array):
    """
    Time: Worst case O(n^2)
    Space: O(1)
    """
    is_sorted = False
    num_swaps = 0

    while not is_sorted:
        is_sorted = True

        for idx in range(len(array) - 1 - num_swaps):
            if array[idx] > array[idx + 1]:
                swapElements(idx, idx + 1, array)
                is_sorted = False

        num_swaps += 1

    return array


def swapElements(i, j, array):
    array[i], array[j] = array[j], array[i]
