"""
283. Move Zeroes
Easy
14.7K
371
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

0,1,0,3,12

1,0,0,3,12

1,3,0,0,12


1,3,0,0,12

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""
from typing import List

def moveZeroesList(nums: List[int]) -> None:
    nonZeros = [n for n in nums if n != 0]
    nums[0:len(nonZeros)] = nonZeros
    nums[len(nonZeros):] = [0] * (len(nums) - len(nonZeros))


def moveZeroes(nums: List[int]) -> None:
    zeroIdx, nonZeroIdx = -1, -1
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            if zeroIdx == -1:
                zeroIdx = i
        else:
            if i > zeroIdx and zeroIdx > -1:
                nums[zeroIdx], nums[i] = nums[i], nums[zeroIdx]
                zeroIdx = zeroIdx + 1
        i = i + 1


nums = [0,0]

# moveZeroesList(nums)
moveZeroes(nums)
print(nums)