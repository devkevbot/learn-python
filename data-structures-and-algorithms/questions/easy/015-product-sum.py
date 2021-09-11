"""
Return a sum that is created using the following rules:
An input array is given which consists of integers and nested arrays of integers.
The sum of a given element is multiplied by the depth of nesting, starting at 1.
"""


def productSum(array, multiplier=1):
    """
    Time complexity: O(n), where n is the number of integers.
    Space complexity: O(d), where d is the greatest depth of special arrays in the array.
    """
    special_sum = 0

    for element in array:
        if type(element) is int:
            special_sum += element
        elif type(element) is list:
            special_sum += productSum(element, multiplier + 1)

    return special_sum * multiplier
