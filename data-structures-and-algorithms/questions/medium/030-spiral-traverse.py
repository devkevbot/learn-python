def spiralTraverse(array):
    """
    Time: O(k) where k is the number of elements in the matrix
    Space: O(k)
    """

    start_row = 0
    end_row = len(array) - 1  # n rows

    start_col = 0
    end_col = len(array[0]) - 1  # m cols

    spiral = []

    while start_row <= end_row and start_col <= end_col:
        for col in range(start_col, end_col + 1):
            spiral.append(array[start_row][col])

        for row in range(start_row + 1, end_row + 1):
            spiral.append(array[row][end_col])

        for col in reversed(range(start_col, end_col)):
            if start_row == end_row:
                break
            spiral.append(array[end_row][col])

        for row in reversed(range(start_row + 1, end_row)):
            if start_col == end_col:
                break
            spiral.append(array[row][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return spiral
