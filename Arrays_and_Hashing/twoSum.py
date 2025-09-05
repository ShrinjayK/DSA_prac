from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        difference_mapping = {}
        for i, a in enumerate(nums):
            difference = target - a
            if difference in difference_mapping:
                return [difference_mapping[difference], i]
            difference_mapping[a] = i