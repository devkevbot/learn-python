"""
Determine if the characters in document can be made up of the characters array.
Duplicates are allowed.
"""


def generateDocument(characters, document):
    """
    Time: O(n + m)
    Space: O(c) where c is the number of unique characters
    """
    possible_characters = {}

    for char in characters:
        if char not in possible_characters:
            possible_characters[char] = 0

        possible_characters[char] += 1

    for char in document:
        if char not in possible_characters or possible_characters[char] == 0:
            return False

        possible_characters[char] -= 1

    return True
