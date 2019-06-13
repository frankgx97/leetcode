class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)):
            if prices[i:]:
                delta = max(prices[i:]) - prices[i]
                m = max(delta, m)
        return m
