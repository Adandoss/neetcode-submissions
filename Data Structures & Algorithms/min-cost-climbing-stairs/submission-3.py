class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def helper(cost: List[int], index: int) -> int:
            if index >= len(cost):
                return 0

            if cache[index] == -1:
                cache[index] = cost[index] + min(helper(cost, index+1), helper(cost, index+2))

            return cache[index]

        return min(helper(cost, 0), helper(cost, 1))

