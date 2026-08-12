class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def helper(index: int) -> int:
            if index > len(nums) - 1:
                return 0
            if cache[index] == -1:
                cache[index] = nums[index] + max(helper(index + 2), helper(index + 3))
            return cache[index]
        return max(helper(0), helper(1))