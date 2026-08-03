class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i, j = 0, len(heights)-1
        
        while i < j:
            current_area = (j-i) * min(heights[i], heights[j])
            max_area = max(current_area, max_area)
            i, j = (i + 1, j) if heights[i] < heights[j] else (i, j - 1)

        return max_area