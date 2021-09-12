def firstDuplicateValue(array):
    """
    Time: O(n) where n is the length of the input array
    Space: O(n)
    """
    seen = set()

    for number in array:
        if number in seen:
            return number
        seen.add(number)
    return -1


def firstDuplicateValue(array):
    """
    Time: O(n) where n is the length of the input array
    Space: O(1)
    """

    for number in array:
        abs_value = abs(number)

        if array[abs_value - 1] < 0:
            return (
                abs_value  # We've seen this number before and have marked it negative!
            )

        array[abs_value - 1] *= -1

    return -1  # No duplicates
