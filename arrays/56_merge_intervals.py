"""
Problem: 56 Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104


Algorithm:
(Using Sorting)
1. Sort the intervals with the interval start
2. Loop over the sorted intervals:
    1. Commpare the end of last result is greater than start of current interval
        if True:
        Merge the intervals such that end of last interval in result is set to end of current interval
        Else:
        Add the interval to the end of result.
Return the results array
"""



def merge_interval_sorted(intervals):
    intervals = sorted(intervals, key= lambda x : x[0])
    print(intervals)
    result = [intervals[0]]

    for interval in intervals:
        if result[-1][1] >= interval[0]:
            result[-1][1] = max(result[-1][1],interval[1])
        else:
            result.append(interval)

    return result


print(merge_interval_sorted([[1,2],[3,4],[5,6],[7,9],[0,10]]))