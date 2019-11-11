class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        find the min before each item - ac
        maintain a "min" var, and a "max_porfit" var
        iterate the array, if current < min, update min,
        else update the max_profit 
        '''
        if not prices:
            return 0
        mi = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            elif prices[i] - mi > max_profit:
                max_profit = prices[i] - mi
        return max_profit
