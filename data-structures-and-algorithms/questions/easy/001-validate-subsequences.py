"""
Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
"""


def isValidSubsequence(array, sequence):
    # Write your code here.
    num_matches = 0
    desired_num_matches = len(sequence)
    curr_sequence_index = 0
    for num in array:
        if (
            curr_sequence_index < desired_num_matches
            and num == sequence[curr_sequence_index]
        ):
            num_matches += 1
            curr_sequence_index += 1

    return num_matches == desired_num_matches
