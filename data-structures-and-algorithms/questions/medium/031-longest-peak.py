def longestPeak(array):
    """
    Time: O(n) where n is the length of the array
    Space: O(1)
    """
    longest_peak_length = 0

    curr_pos = 1

    while curr_pos < len(array) - 1:
        is_peak = (
            array[curr_pos - 1] < array[curr_pos]
            and array[curr_pos] > array[curr_pos + 1]
        )

        if not is_peak:
            curr_pos += 1
            continue

        left_pos = curr_pos - 2

        while left_pos >= 0 and array[left_pos] < array[left_pos + 1]:
            left_pos -= 1

        right_pos = curr_pos + 2

        while right_pos <= len(array) - 1 and array[right_pos] < array[right_pos - 1]:
            right_pos += 1

        current_peak_length = right_pos - left_pos - 1
        longest_peak_length = max(current_peak_length, longest_peak_length)

        curr_pos = right_pos

    return longest_peak_length
