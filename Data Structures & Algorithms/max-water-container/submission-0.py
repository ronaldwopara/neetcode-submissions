from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        prev_max = 0

        while left < right:
            distance = right - left
            height = min(heights[left], heights[right])
            curr_max = distance * height
            prev_max = max(prev_max, curr_max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return prev_max

            

            

            
        