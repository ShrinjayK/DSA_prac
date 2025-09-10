from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        left, right = 0, len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            most = max(area, most)
            if heights[left] < heights[right]:
                left  += 1
            else:
                right -= 1
        return most
