class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result