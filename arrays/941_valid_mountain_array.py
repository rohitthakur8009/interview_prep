"""
941. Valid Mountain Array
Easy
2.7K
170
Companies
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true


Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104

"""

from typing import List


def valid_mountain_array(arr: List[int]) -> bool:
    if len(arr) <= 2 or arr[0] >= arr[1]:
        return False
    up = True

    for i in range(1, len(arr)):
        if up:
            if i == len(arr) - 1:
                return False
            if arr[i] == arr[i + 1]:
                return False
            if arr[i] > arr[i + 1]:
                up = False
        else:
            if arr[i - 1] <= arr[i]:
                return False
    return True

print(valid_mountain_array([6,7,8,6]))

print(valid_mountain_array([3,5,5,3]))
print(valid_mountain_array([2,1]))

