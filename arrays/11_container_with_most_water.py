"""
11. Container With Most Water
Medium
25.8K
1.4K
Companies
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

Approach:
    Place indices at start and end of list..
    Loop untill start reaches the end:
        Calculate area between these 2 heights
            Area = min of height of start and end * (end - start)
                is area is the highest area found so far save it in result
        shift the start pointer right if the next tower is higher than current
            else shift the end pointer to the left.

    Return the result.
"""

from typing import List


def maxArea(height: List[int]) -> int:
    area = 0
    start, end = 0, len(height) - 1

    while start < end:
        curr_area = (end - start) * min(height[start], height[end])
        area = max(area, curr_area)
        if height[start] < height[end]:
            start = start + 1
        else:
            end = end - 1
    return area


print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))