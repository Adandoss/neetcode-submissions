class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right and left >= 0 and right <= len(nums):
            mid = (right + left) // 2
            if nums[mid] == target: return mid
            elif nums[mid] > target: right = mid
            elif nums[mid] < target: left = mid + 1
        return -1
