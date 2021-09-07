"""
String are immutable. Therefore, we can't manipulate them in-place.
However, strings are sequence - they're indexable, sliceable, and iterable.
"""


def slice_a_string(string):
    all_characters_1 = string[::]
    all_characters_2 = string[:]
    print(all_characters_1 == all_characters_2)

    every_other_character = string[::2]
    print(every_other_character)

    every_other_character_from_one = string[1::2]
    print(every_other_character_from_one)

    all_reversed = string[::-1]
    print(all_reversed)

    all_reversed_every_other_character = string[::-2]
    print(all_reversed_every_other_character)

    all_reversed_every_other_character_from_last = string[-2::-2]
    print(all_reversed_every_other_character_from_last)


slice_a_string("AaBbCcDd")


def common_str_methods(string):
    capitalized = string.capitalize()
    print(capitalized)

    lower_case = string.casefold()
    print(lower_case)

    title = string.title()
    print(title)

    o_count = string.count("o")
    print(f"The lowercase letter 'o' appears {o_count} times")

    ends_with_roofus = string.endswith("roofus")
    print(f"Does the string end with 'roofus'? {ends_with_roofus}")


print()
common_str_methods("my DOG is named roofus")

reversed_string = reversed("olleH")
for letter in reversed_string:
    print(letter, end="")
