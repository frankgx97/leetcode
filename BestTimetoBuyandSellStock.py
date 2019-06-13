class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 99999999
        max_profit = 0
        for i in prices:
            min_price = min(min_price, i)
            profit = i - min_price
            max_profit = max(max_profit, profit)
        return max_profit
