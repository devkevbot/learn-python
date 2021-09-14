"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
"""


def isValidSubsequence(array, sequence):
    """
    Time: O(n) where n is the number of elements in the array
    Space: O(1)
    """
    sequence_idx = 0
    current_match_count = 0
    desired_match_count = len(sequence)

    for number in array:
        if number == sequence[sequence_idx]:
            current_match_count += 1
            sequence_idx += 1
            if current_match_count == desired_match_count:
                return True

    return False
