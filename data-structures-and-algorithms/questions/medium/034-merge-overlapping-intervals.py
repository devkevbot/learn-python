def mergeOverlappingIntervals(intervals):
    """
    Time: O(nlogn)
    Space: O(n)
    """
    if len(intervals) < 2:
        return intervals

    intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_interval = intervals[0]
    merged_intervals.append(current_interval)

    for interval in intervals:
        _, current_end = current_interval
        next_start, next_end = interval

        if current_end >= next_start:
            current_interval[1] = max(current_end, next_end)
        else:
            current_interval = interval
            merged_intervals.append(current_interval)

    return merged_intervals
