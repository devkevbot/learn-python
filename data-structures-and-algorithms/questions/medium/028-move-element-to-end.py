def moveElementToEnd(array, toMove):
    """
    Time: O(n) - we loop through array once
    Space: O(1) - we do not store any new structures or recurse
    """
    start_idx = 0
    end_idx = len(array) - 1

    while start_idx < end_idx:
        if array[start_idx] == toMove:
            swap(start_idx, end_idx, array)
            end_idx -= 1
        if array[start_idx] != toMove:
            start_idx += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
