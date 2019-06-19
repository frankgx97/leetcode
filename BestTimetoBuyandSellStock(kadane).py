class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 99999999
        global_max_profit = 0
        for i in prices:
            min_price = min(min_price, i)
            local_max_profit = i - min_price
            global_max_profit = max(global_max_profit, local_max_profit)
        return global_max_profit
