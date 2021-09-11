def moveElementToEnd(array, toMove):
    """
    Time: O(n) - we loop through array once
    Space: O(1) - we do not store any new structures or recurse
    """
    startIndex = 0
    endIndex = len(array) - 1

    while startIndex < endIndex:
        if array[startIndex] == toMove:
            swap(startIndex, endIndex, array)
            endIndex -= 1
        if array[startIndex] != toMove:
            startIndex += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
