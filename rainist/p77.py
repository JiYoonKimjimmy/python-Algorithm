def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda i: i[0])
    merged_intervals = []

    for interval in sorted_intervals:
        if merged_intervals and interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1] = (merged_intervals[-1][0], max(interval[1], merged_intervals[-1][1]))
        else:
            merged_intervals.append(interval)

    print(merged_intervals)

    return merged_intervals


intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (22, 27)]
assert merge(intervals) == [(1, 3), (4, 10), (20, 27)]
assert merge(intervals) == [(1, 3), (4, 10), (20, 27)]
