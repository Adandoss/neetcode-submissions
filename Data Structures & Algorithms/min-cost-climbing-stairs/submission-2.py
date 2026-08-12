class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cashe = [-1]*len(cost)
        def helper(cost: List[int], index: int) -> int:
            if index < len(cost):
                if cashe[index] == -1:
                    cashe[index] = cost[index] + min(helper(cost, index+1), helper(cost, index+2))
                return cashe[index]
            else:
                return 0

        return min(helper(cost, 0), helper(cost, 1))

