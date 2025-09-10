from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[right]:
                right = middle - 1
            else:
                left = middle
        return nums[left]