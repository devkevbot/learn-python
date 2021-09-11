"""
Return the index of a string's first non-repeating-character.
That is, the first character which appears only once in the whole string.
Input strings consists only of lowercase English-alphabet characters.
"""


def firstNonRepeatingCharacter(string):
    """
    Time: O(n) where n is the number of characters in the string
    Space: O(1) because we are limited to 26 lowercase letters
    """
    characters_seen = {}

    for character in string:
        if character not in characters_seen:
            characters_seen[character] = 0

        characters_seen[character] += 1

    for index in range(len(string)):
        value_at = string[index]
        if characters_seen[value_at] == 1:
            return index

    return -1
