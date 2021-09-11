"""
Given an input array of integers, return an array of all triplets which
sum up to a target sum.

The triplets should be sorted in ascending order.
"""


def threeNumberSum(array, targetSum):
    """
    Time: O(n^2) - iterate through main array and for each number, we iterate through the rest of the array.
    Space: O(n)
    """

    array.sort()
    three_number_sums = []

    for idx in range(len(array)):
        left_ptr = idx + 1
        right_ptr = len(array) - 1

        while left_ptr < right_ptr:
            current_sum = array[idx] + array[left_ptr] + array[right_ptr]

            if current_sum == targetSum:
                three_number_sums.append(
                    [array[idx], array[left_ptr], array[right_ptr]]
                )
                left_ptr += 1
                right_ptr -= 1
            elif current_sum < targetSum:
                left_ptr += 1
            else:
                right_ptr -= 1

    return three_number_sums
