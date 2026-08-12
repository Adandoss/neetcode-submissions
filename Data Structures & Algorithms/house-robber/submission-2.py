class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * 4

        for i in range(len(nums) - 1, -1, -1):
            dp = [dp[-1]] + dp[:-1]
            dp[0] = nums[i] + max(dp[2], dp[3])


        return max(dp[0], dp[1])