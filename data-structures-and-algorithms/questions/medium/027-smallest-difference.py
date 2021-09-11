"""
Given two arrays of integers, return the pair of elements (one from each
array) which have the smallest difference.
"""


def smallestDifference(arrayOne, arrayTwo):
    """
    Time: O(nlog(n) + mlog(m)), where n is the length of arrayOne and m is the length of arrayTwo
    Space: O(1)
    """
    arrayOne.sort()
    arrayTwo.sort()

    arr_one_ptr = 0
    arr_two_ptr = 0

    smallest_diff_amt = float("inf")
    smallest_elements = []

    while arr_one_ptr < len(arrayOne) and arr_two_ptr < len(arrayTwo):
        arr_one_val = arrayOne[arr_one_ptr]
        arr_two_val = arrayTwo[arr_two_ptr]

        curr_diff = abs(arr_one_val - arr_two_val)

        if curr_diff < smallest_diff_amt:
            smallest_diff_amt = curr_diff
            smallest_elements = [arr_one_val, arr_two_val]

        if arr_one_val > arr_two_val:
            arr_two_ptr += 1
        else:
            arr_one_ptr += 1

    return smallest_elements
