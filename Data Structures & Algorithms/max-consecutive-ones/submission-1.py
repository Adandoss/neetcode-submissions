class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0

        for n in nums:
            cnt = cnt + 1 if n else 0
            res = max(res, cnt)

        return res