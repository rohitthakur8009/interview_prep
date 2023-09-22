"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

1. Copy all intervals before overlap. Detect overlap if end of interval is greater than start of new Interval
2. Start of interval is min(overlapping Interval, new Interval)
3. Start looping over next intervals to find the end of interval:
    if new Target end < Current Interval Start:
        Add new Target Interval to result
        Copy all remaining intervals
    if new Target interval end < Current Interval End:
        Add Current Interval End to result
        Copy all remaining intervals

"""
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(newInterval) == 0:
        return [newInterval]
    if newInterval[1] < intervals[0][0]:
        return [newInterval] + intervals
    result = []
    merging = False
    merged = []
    mergeIdx = 0
    for idx, interval in enumerate(intervals):
        if not merging:
            if interval[1] < newInterval[0]:
                result.append(interval)
            else:
                merging = True
                merged.append(min(interval[0], newInterval[0]))
                if newInterval[1] < interval[0]:
                    result.append(newInterval)
                    result.extend(intervals[idx:])
                    return result
                else:
                    mergeIdx = idx
                    break
    if not merging:
        return intervals + [newInterval]
    while mergeIdx < len(intervals):
        if newInterval[1] < intervals[mergeIdx][0]:
            merged.append(max(intervals[mergeIdx-1][1], newInterval[1]))
            result.append(merged)
            result.extend(intervals[mergeIdx:])
            return result
        mergeIdx = mergeIdx + 1
    if len(merged) == 1:
        merged.append(max(newInterval[1], intervals[-1][1]))
        result.append(merged)
    return result


print(insert(intervals = [[1,5]], newInterval = [6,8]))



