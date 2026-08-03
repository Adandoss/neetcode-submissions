class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i, j = 0, len(heights)-1
        while i < j:
            current_area = (j-i) * min(heights[i], heights[j])

            max_area = max(current_area, max_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area