"""Find the minimum amount of time that queries have to wait for."""


def minimumWaitingTime(queries):
    """
    Time: O(nlogn) - array is sorted
    Space: O(1) - no additional arrays are needed
    """
    queries.sort()

    current_wait = 0
    wait_sum = 0

    for index in range(1, len(queries)):
        current_wait += queries[index - 1]
        wait_sum += current_wait

    return wait_sum
