class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        for j in range(1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])
            if prices[i] > prices[j] and j != len(prices) - 1:
                i = j
        return max_profit
            
            