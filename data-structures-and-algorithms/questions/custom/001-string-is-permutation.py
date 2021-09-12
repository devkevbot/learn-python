from test import run_test


def string_is_permutation(source, target):
    """
    Returns True if target is a permutation of source, False otherwise.
    Time: O(n) where n is length of the longer of the two input strings
    Space: O(a + b) where a is the number of unique characters in source
    and b is the number of unique characters in target
    """
    source_char_frequency = {}

    for character in source:
        if character not in source_char_frequency:
            source_char_frequency[character] = 0
        source_char_frequency[character] += 1

    target_char_frequency = {}

    for character in target:
        if character not in target_char_frequency:
            target_char_frequency[character] = 0
        target_char_frequency[character] += 1

    for key in source_char_frequency:
        if key in source_char_frequency and key not in target_char_frequency:
            return False
        if source_char_frequency[key] != target_char_frequency[key]:
            return False

    return True


test_inputs = [
    ["a", "a", True],
    ["ab", "ab", True],
    ["ab", "ba", True],
    ["abc", "cba", True],
    ["abcd", "dcb", False],
    ["", "", True],
    ["a", "", False],
    ["abc", "a", False],
    ["---", "-_-", False],
    ["123456789", "5678901234", True],
]

run_test(
    string_is_permutation,
    test_inputs,
)
