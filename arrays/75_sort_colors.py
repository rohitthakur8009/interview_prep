"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List


def sort_colors(nums: List[int]) -> None:
    l, r = 0, len(nums) - 1
    while l < r:
        while l < len(nums) and nums[l] != 2:
            l = l + 1
        while r > 0 and nums[r] == 2:
            r = r - 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
    l, r = 0, len(nums) - 1
    while r > 0 and nums[r] == 2:
        r = r - 1
    while l < r:
        while l < len(nums) and nums[l] != 1:
            l = l + 1
        while  r > 0 and nums[r] == 1:
            r = r - 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]



nums = [0,1,2,2,2,1,1,1, 0]

sortColors(nums)
print(nums)

