"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.



Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]


1,2,3,4,5
1,2,3,5,4
1,2,5,3,4
1,5,2,3,4

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100


Approach:
1. Start at the end of the array find the first element such that the current element is greater than the element before it.
2. Record the pointer where this happens. (i)
3. If pointer is 0, (means the array is reverse sorted), return the reverse of array as the result.
4. Else starting from the i, find the least great element that is greater than the i-1th element in the subarray.
5. Swap the i-1 element with the least great element. Sort the remaining subarray.

"""

from typing import List


def nextPermutation(nums: List[int]) -> None:
    i = len(nums) - 1
    while nums[i] <= nums[i - 1] and i > 0:
        i = i - 1
    if i == 0:
        nums.reverse()

    j = i
    curr = nums[i]
    idx = i + 1
    while idx < len(nums):
        if curr > nums[idx] > nums[i - 1]:
            j = idx
            curr = nums[idx]
        idx = idx + 1

    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    nums[i:] = sorted(nums[i:])

nums = [1,1,5]

for _ in range(10):
    nextPermutation(nums)
    print(nums)