"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order.
If no two numbers sum to the largest sum, the function should return an empty array.
"""


def twoNumberSum(array, targetSum):
    """
    Naive for-loop approach
    O(n^2) time and O(1) space
    """
    # Write your code here.
    for i in range(len(array)):
        for j in range(1, len(array)):
            if array[i] + array[j] == targetSum and i != j:
                return [array[i], array[j]]
    return []


def twoNumberSum(array, targetSum):
    """
    Hash table approach
    O(n) time and O(n) space
    """
    # Write your code here.
    # Know that x + y = targetSum
    stored_numbers = {}
    for x in array:
        stored_numbers[x] = True
        y = targetSum - x
        if y != x and y in stored_numbers:
            return [x, targetSum - x]
    return []


def twoNumberSum(array, targetSum):
    """
    Pointer approach
    O(nlogn) time and O(1) space
    """
    left_pos = 0
    right_pos = len(array) - 1

    array.sort()

    while left_pos < right_pos:
        left_val = array[left_pos]
        right_val = array[right_pos]

        current_sum = left_val + right_val

        if current_sum == targetSum:
            return [left_val, right_val]
        elif current_sum > targetSum:
            right_pos -= 1
        else:
            left_pos += 1

    return []
