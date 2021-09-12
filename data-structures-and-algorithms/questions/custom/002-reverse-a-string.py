from test import run_test

"""
Without using built-in language functions, write a function which takes
in a string and returns its reversed counterpart.
"""


def reverse_string(string):
    ptr = len(string) - 1

    reversed_chars = []

    while ptr >= 0:
        reversed_chars.append(string[ptr])
        ptr -= 1

    return "".join(reversed_chars)


test_inputs = [
    ["hello", "olleh"],
    ["", ""],
    ["1234", "4321"],
]

run_test(
    reverse_string,
    test_inputs,
)
